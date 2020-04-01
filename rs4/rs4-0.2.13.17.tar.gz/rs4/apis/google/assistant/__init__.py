# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sample that implements a gRPC client for the Google Assistant API."""

import concurrent.futures
import json
import logging
import os
import os.path
import pathlib2 as pathlib
import sys
import time
import uuid
import multiprocessing
import click
import grpc
import google.auth.transport.grpc
import google.auth.transport.requests
import google.oauth2.credentials
import random
import shutil
from .... import pathtool
from google.assistant.embedded.v1alpha2 import (
    embedded_assistant_pb2,
    embedded_assistant_pb2_grpc
)
from tenacity import retry, stop_after_attempt, retry_if_exception
from .grpc import (
    assistant_helpers,
    audio_helpers,
    browser_helpers,
    device_helpers
)
from . import device_register

ASSISTANT_API_ENDPOINT = 'embeddedassistant.googleapis.com'
END_OF_UTTERANCE = embedded_assistant_pb2.AssistResponse.END_OF_UTTERANCE
DIALOG_FOLLOW_ON = embedded_assistant_pb2.DialogStateOut.DIALOG_FOLLOW_ON
CLOSE_MICROPHONE = embedded_assistant_pb2.DialogStateOut.CLOSE_MICROPHONE
PLAYING = embedded_assistant_pb2.ScreenOutConfig.PLAYING
DEFAULT_GRPC_DEADLINE = 60 * 3 + 5


class SampleAssistant(object):
    """Sample Assistant that supports conversations and device actions.

    Args:
      device_model_id: identifier of the device model.
      device_id: identifier of the registered device instance.
      conversation_stream(ConversationStream): audio stream
        for recording query and playing back assistant answer.
      channel: authorized gRPC channel for connection to the
        Google Assistant API.
      deadline_sec: gRPC deadline in seconds for Google Assistant API call.
      device_handler: callback for device actions.
    """

    def __init__(self, language_code, device_model_id, device_id,
                 conversation_stream, display,
                 channel, deadline_sec, device_handler):
        self.language_code = language_code
        self.device_model_id = device_model_id
        self.device_id = device_id
        self.conversation_stream = conversation_stream
        self.display = display

        # Opaque blob provided in AssistResponse that,
        # when provided in a follow-up AssistRequest,
        # gives the Assistant a context marker within the current state
        # of the multi-Assist()-RPC "conversation".
        # This value, along with MicrophoneMode, supports a more natural
        # "conversation" with the Assistant.
        self.conversation_state = None
        # Force reset of first conversation.
        self.is_new_conversation = True

        # Create Google Assistant API gRPC client.
        self.assistant = embedded_assistant_pb2_grpc.EmbeddedAssistantStub(
            channel
        )
        self.deadline = deadline_sec

        self.device_handler = device_handler

    def __enter__(self):
        return self

    def __exit__(self, etype, e, traceback):
        if e:
            return False
        self.conversation_stream.close()

    def is_grpc_error_unavailable(e):
        is_grpc_error = isinstance(e, grpc.RpcError)
        if is_grpc_error and (e.code() == grpc.StatusCode.UNAVAILABLE):
            logging.error('grpc unavailable error: %s', e)
            return True
        return False

    @retry(reraise=True, stop=stop_after_attempt(3), retry=retry_if_exception(is_grpc_error_unavailable))
    def assist(self):
        """Send a voice request to the Assistant and playback the response.

        Returns: True if conversation should continue.
        """
        continue_conversation = False
        device_actions_futures = []

        self.conversation_stream.start_recording()
        logging.info('Recording audio request.')

        def iter_log_assist_requests():
            for c in self.gen_assist_requests():
                assistant_helpers.log_assist_request_without_audio(c)
                yield c
            logging.debug('Reached end of AssistRequest iteration.')

        question = ''
        supplemental_display_text = ''
        detail = ''
        # This generator yields AssistResponse proto messages
        # received from the gRPC Google Assistant API.
        for resp in self.assistant.Assist(iter_log_assist_requests(), self.deadline):
            assistant_helpers.log_assist_response_without_audio(resp)
            if resp.event_type == END_OF_UTTERANCE:
                logging.info('End of audio request detected.')
                logging.info('Stopping recording.')
                self.conversation_stream.stop_recording()
            if resp.speech_results:
                logging.info('Transcript of user request: "%s".',
                             ' '.join(r.transcript
                                      for r in resp.speech_results))
            if len(resp.audio_out.audio_data) > 0:
                self.conversation_stream.write(resp.audio_out.audio_data)
                #if not self.conversation_stream.playing:
                #    self.conversation_stream.stop_recording()
                #    #self.conversation_stream.start_playback()
                #    logging.info('Playing assistant response.')
            if resp.dialog_state_out.conversation_state:
                conversation_state = resp.dialog_state_out.conversation_state
                logging.debug('Updating conversation state.')
                self.conversation_state = conversation_state
            #if resp.dialog_state_out.volume_percentage != 0:
            #    volume_percentage = resp.dialog_state_out.volume_percentage
            #    logging.info('Setting volume to %s%%', volume_percentage)
            #    self.conversation_stream.volume_percentage = volume_percentage
            #if resp.dialog_state_out.microphone_mode == DIALOG_FOLLOW_ON:
                #continue_conversation = True
                #logging.info('Expecting follow-on query from user.')
            #elif resp.dialog_state_out.microphone_mode == CLOSE_MICROPHONE:
            #    continue_conversation = False
            if resp.device_action.device_request_json:
                device_request = json.loads(
                    resp.device_action.device_request_json
                )
                fs = self.device_handler(device_request)
                if fs:
                    device_actions_futures.extend(fs)

            # if self.display and resp.screen_out.data:
            #    system_browser = browser_helpers.system_browser
            #    system_browser.display(resp.screen_out.data)

            if resp.speech_results:
                question = ' '.join(r.transcript for r in resp.speech_results)
            if resp.dialog_state_out.supplemental_display_text and not supplemental_display_text:
                supplemental_display_text = resp.dialog_state_out.supplemental_display_text
            if resp.screen_out.data and not detail:
                detail = resp.screen_out.data

        if len(device_actions_futures):
            logging.info('Waiting for device executions to complete.')
            concurrent.futures.wait(device_actions_futures)

        logging.info('Finished playing assistant response.')
        #self.conversation_stream.stop_playback()
        return question, supplemental_display_text, detail

    def gen_assist_requests(self):
        """Yields: AssistRequest messages to send to the API."""

        config = embedded_assistant_pb2.AssistConfig(
            audio_in_config=embedded_assistant_pb2.AudioInConfig(
                encoding='LINEAR16',
                sample_rate_hertz=self.conversation_stream.sample_rate,
            ),
            audio_out_config=embedded_assistant_pb2.AudioOutConfig(
                encoding='LINEAR16',
                sample_rate_hertz=self.conversation_stream.sample_rate,
                volume_percentage=self.conversation_stream.volume_percentage,
            ),
            dialog_state_in=embedded_assistant_pb2.DialogStateIn(
                language_code=self.language_code,
                conversation_state=self.conversation_state,
                is_new_conversation=self.is_new_conversation,
            ),
            device_config=embedded_assistant_pb2.DeviceConfig(
                device_id=self.device_id,
                device_model_id=self.device_model_id,
            )
        )
        if self.display:
            config.screen_out_config.screen_mode = PLAYING
        # Continue current conversation with later requests.
        self.is_new_conversation = False
        # The first AssistRequest must contain the AssistConfig
        # and no audio data.
        yield embedded_assistant_pb2.AssistRequest(config=config)
        for data in self.conversation_stream:
            # Subsequent requests need audio data, but not config.
            yield embedded_assistant_pb2.AssistRequest(audio_in=data)

logging.basicConfig(level=logging.INFO)
api_endpoint = ASSISTANT_API_ENDPOINT
device_handler = None
tmpdir = '/tmp/rs4/google-assistant'
pathtool.mkdir (tmpdir)

def set_device (project_id_, device_model_id_):
    global api_endpoint, device_model_id, device_id, grpc_channel, device_handler

    project_id = project_id_
    # Load OAuth 2.0 credentials.
    try:
        with open(os.path.join(click.get_app_dir('google-oauthlib-tool'), 'credentials.json'), 'r') as f:
            credentials = google.oauth2.credentials.Credentials(token=None, **json.load(f))
    except Exception as e:
        raise
    device_id, device_model_id = device_register.register (api_endpoint, project_id, device_model_id_)
    http_request = google.auth.transport.requests.Request()
    credentials.refresh(http_request)
    grpc_channel = google.auth.transport.grpc.secure_authorized_channel (credentials, http_request, api_endpoint)
    device_handler = device_helpers.DeviceRequestHandler (device_id)

audio_sample_rate = audio_helpers.DEFAULT_AUDIO_SAMPLE_RATE
audio_sample_width = audio_helpers.DEFAULT_AUDIO_SAMPLE_WIDTH
audio_iter_size = audio_helpers.DEFAULT_AUDIO_ITER_SIZE
audio_block_size = audio_helpers.DEFAULT_AUDIO_DEVICE_BLOCK_SIZE
audio_flush_size = audio_helpers.DEFAULT_AUDIO_DEVICE_FLUSH_SIZE
lock = multiprocessing.Lock ()

def send (audio_source, lang = 'ko-KR', output_audio_file = None, once = True, display = True, verbose = False, *args, **kwargs):
    global grpc_channel, device_model_id, device_id, lock, device_handler

    output_audio_file =  output_audio_file or os.path.join (tmpdir, 'out-' + str (random.random ()) [2:] + '.wav')
    audio_sink = audio_helpers.WaveSink(
        open(output_audio_file, 'wb'),
        sample_rate=audio_sample_rate,
        sample_width=audio_sample_width
    )

    # Create conversation stream with the given audio source and sink.
    conversation_stream = audio_helpers.ConversationStream (
        source = audio_source,
        sink = audio_sink,
        iter_size = audio_iter_size,
        sample_width = audio_sample_width,
    )

    with lock:
        # ensure single thread
        with SampleAssistant (lang, device_model_id, device_id,
                            conversation_stream, display,
                            grpc_channel, DEFAULT_GRPC_DEADLINE,
                            device_handler) as assistant:

            question, supplemental_display_text, detail = assistant.assist ()
            return AssistResponse (question, supplemental_display_text, detail, output_audio_file)

def send_wav (input_audio_file, lang = 'ko-KR', output_audio_file = None, once = True, display = True, verbose = False, *args, **kwargs):
    audio_source = audio_helpers.WaveSource(
        open(input_audio_file, 'rb'),
        sample_rate=audio_sample_rate,
        sample_width=audio_sample_width
    )
    return send (audio_source, lang, output_audio_file, once, display, verbose, *args, **kwargs)
from_audio = send_wav

def use_device (device, lang = 'ko-KR', output_audio_file = None, once = True, display = True, verbose = False, *args, **kwargs):
    audio_source = audio_helpers.SoundDeviceStream(
        sample_rate=audio_sample_rate,
        sample_width=audio_sample_width,
        block_size=audio_block_size,
        flush_size=audio_flush_size,
        device = device
    )
    resp = send (audio_source, lang, output_audio_file, once, display, verbose, *args, **kwargs)
    audio_source.close ()
    return resp

class AssistResponse:
    def __init__ (self, question, supplemental_display_text, detail, output_audio_file):
        self.question = question
        self.supplemental_display_text = supplemental_display_text
        self.detail = detail
        self.audio = output_audio_file

    def move (self, target):
        shutil.move (self.audio, target)
    save = move

    def remove (self):
        if os.path.isfile (self.audio):
            os.remove (self.audio)

if __name__ == "__main__":
    project_id = ''
    device_model_id = ''
    set_device (project_id, device_model_id)
    use_device (None)

