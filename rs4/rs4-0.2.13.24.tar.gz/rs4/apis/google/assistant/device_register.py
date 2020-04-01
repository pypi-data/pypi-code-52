import logging
import sys
import json
import google.auth.transport.requests
import click
import os

def register (api_endpoint, project_id, device_model_id, device_config = None):
    device_config = device_config or os.path.join (click.get_app_dir('googlesamples-assistant'), 'device_config.json')
    try:
        with open(device_config) as f:
            device = json.load(f)
            device_id = device['id']
            device_model_id = device['model_id']
            logging.info("Using device model %s and device id %s",
                            device_model_id,
                            device_id)
        
    except Exception as e:
        logging.warning('Device config not found: %s' % e)
        logging.info('Registering device')
        if not device_model_id:
            logging.error('Option --device-model-id required '
                            'when registering a device instance.')
            sys.exit(-1)
        if not project_id:
            logging.error('Option --project-id required '
                            'when registering a device instance.')
            sys.exit(-1)
        device_base_url = (
            'https://%s/v1alpha2/projects/%s/devices' % (api_endpoint,
                                                            project_id)
        )
        device_id = str(uuid.uuid1())
        payload = {
            'id': device_id,
            'model_id': device_model_id,
            'client_type': 'SDK_SERVICE'
        }
        session = google.auth.transport.requests.AuthorizedSession(
            credentials
        )
        r = session.post(device_base_url, data=json.dumps(payload))
        if r.status_code != 200:
            logging.error('Failed to register device: %s', r.text)
            sys.exit(-1)
        logging.info('Device registered: %s', device_id)
        pathlib.Path(os.path.dirname(device_config)).mkdir(exist_ok=True)
        with open(device_config, 'w') as f:
            json.dump(payload, f)
    
    return device_id, device_model_id
    