# auto generated by update_py.py

import threading
import hashlib
import time
import os
from dataclasses import dataclass, field
import zmq
import pandas
from stat import S_ISREG
from typing import List
from collections import defaultdict
from tlclient.linker.fist import Fist
from tlclient.linker.constant import FistType, SubscribeTopic
from tlclient.linker.event import PBEvent
import tlclient.trader.pb_msg as message_pb

@dataclass
class ParamInfoHelper:
    content: str = field(init=False)
    group: str = field(init=False)
    file_stat: os.stat_result = field(init=False)
    digest: bytes = field(init=False)


class ParamServer(Fist):

    _PRODUCER_CONSUMER_ADDR = "inproc://pc-notify"
    _SLEEP_TIME_IN_SECONDS = 0.5

    def __init__(self, name: str, env_name: str, master_addr: str, file_path: str):
        super().__init__(name, FistType.PARAM_SERVER, env_name, master_addr)
        self.use_seperate_queue = True
        self.logger.info(f'param server starting...(file_path){file_path}')
        # the path of param file to be checked
        self._file_path = file_path
        self._file_lock = threading.Lock()
        self._file_stat_digest = defaultdict(ParamInfoHelper)
        # setup producer socket
        self._producer = self._context.socket(zmq.PAIR)
        #self._producer.setsockopt(zmq.ZMQ_CONFLATE, 1)
        self._producer.bind(self._PRODUCER_CONSUMER_ADDR)
        # consumer socket will be created in the consumer thread
        self._consumer: zmq.Socket = None
        self.create_fist()

    def init(self):
        self.set_rep()
        self.set_pub()
        self._pub_t = threading.Thread(target=self._pub_params, name='param_pub', daemon=True)
        self._pub_t.start()
        self._probe_t = threading.Thread(target=self._probe_params, name='param_prober', daemon=True)
        self._probe_t.start()

    def on_req_frame(self, f: PBEvent) -> PBEvent:
        if f.get_msg_type() == message_pb.MSG_TYPE_PARAM_REQ_INFO:
            req = f.get_obj(message_pb.ReqParamInfo)
            if not req.file_names:
                f.set_msg_type(message_pb.MSG_TYPE_PARAM_RSP_INFO)
                rsp = message_pb.RspParamInfo()
                with self._file_lock:
                    for file_name in self._file_stat_digest:
                        pi = rsp.param_infos.add()
                        pi.file_name = file_name
                        pi.content = self._file_stat_digest[file_name].content
                        pi.group = self._file_stat_digest[file_name].group
                f.set_data(rsp)
            else:
                # send the latest content of param file as response
                f.set_msg_type(message_pb.MSG_TYPE_PARAM_RSP_INFO)
                try:
                    with self._file_lock:
                        content = self._file_stat_digest[req.file_name].content
                        group = self._file_stat_digest[file_name].group
                    rsp = message_pb.RspParamInfo()
                    pi = rsp.param_infos.add()
                    pi.file_name = req.file_name
                    pi.content = content
                    pi.group = group
                    f.set_data(rsp)
                except KeyError:
                    f.set_err_id(-2)
        else:
            f.set_err_id(-1)
        return f

    def _pub_params(self):
        self.logger.info(f"{self.fist_name}'s param pub thread started!")
        self._consumer = self._context.socket(zmq.PAIR)
        #self._consumer.setsockopt(zmq.ZMQ_CONFLATE, 1)
        self._consumer.connect(self._PRODUCER_CONSUMER_ADDR)
        while not self.is_stopped():
            try:
                data = self._consumer.recv_multipart()
                rsp = message_pb.RspParamInfo()
                pi = rsp.param_infos.add()
                pi.file_name = data[0]
                pi.content = data[1]
                pi.group = data[2]
                # recv will block until a message arrives,
                self.pub(rsp, message_pb.MSG_TYPE_PARAM_RSP_INFO, 0, topic=SubscribeTopic.NOT_AVAILABLE)
            except zmq.ZMQError as e:
                self.logger.error(f'zmq error (errno){e.errno} (msg){e.msg}')

    def _probe_params(self):
        self.logger.info(f"{self.fist_name}'s param prober started!")
        while not self.is_stopped():
            sleep_time = self._SLEEP_TIME_IN_SECONDS
            try:
                # check whether the file exists first
                if S_ISREG(os.stat(self._file_path).st_mode) == 0:
                    raise FileNotFoundError
                file_dir: str = os.path.dirname(self._file_path)
                master_pd = pandas.read_csv(self._file_path)
                for i in range(len(master_pd.FILE)):
                    f = master_pd.FILE[i]
                    file_path = os.path.join(file_dir, f)
                    file_stat = os.stat(file_path)
                    pd = pandas.read_csv(file_path)
                    content: str = pd.to_csv()
                    group: str = master_pd.GROUP[i]
                    digest: bytes = hashlib.sha256(content.encode()).digest()
                    # then check the modification time and hash value of the file
                    with self._file_lock:
                        if (f not in self._file_stat_digest or (file_stat.st_mtime_ns != self._file_stat_digest[f].file_stat.st_mtime_ns or
                            digest != self._file_stat_digest[f].digest)):
                            self._file_stat_digest[f].content = content
                            self._file_stat_digest[f].group = group
                            self._send_content(content, group, f, mtime_ns=file_stat.st_mtime_ns, digest=digest)

                        self._file_stat_digest[f].file_stat = file_stat
                        self._file_stat_digest[f].digest = digest
            except OSError as e:
                self.logger.error(f'error with {e.filename}! (errno){e.errno} (msg){e.strerror}')
                sleep_time += 1
            except zmq.ZMQError as e:
                self.logger.error(f'zmq error when sending content (errno){e.errno} (msg){e.msg}')
                sleep_time += 1
            finally:
                time.sleep(sleep_time)

    def _send_content(self, content: str, group: str, file_name: str, mtime_ns=None, digest=None):
        self.logger.info(f'got new content from param file (name){file_name} (mtime_ns){mtime_ns} (digest){digest}')
        self._producer.send_string(file_name, flags=zmq.SNDMORE)
        self._producer.send_string(content, flags=zmq.SNDMORE)
        self._producer.send_string(group)

if __name__ == '__main__':
    ps = ParamServer('ps1', 'env1', 'tcp://0.0.0.0:9000', '/shared/tl/strategy/strg_KG_sep/trading_files_strg_KG_sep.csv')
    ps.init()
    ps.start()
    ps.join()