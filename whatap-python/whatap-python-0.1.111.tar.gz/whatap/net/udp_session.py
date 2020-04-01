import threading

import sys, os
import traceback
import time
import logging
import socket
import errno

from whatap.io import DataOutputX
from whatap.net.packet_enum import PacketEnum
from whatap.net.packet_type_enum import PacketTypeEnum
from whatap.net.param_def import ParamDef
from whatap.trace import TraceContextManager


class UdpSession(object):
    s = None
    buffer_arr = []
    thread_lock = threading.Lock()
    read_timeout = 5

    @classmethod
    def udp(cls):
        import socket, struct
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, PacketEnum.PACKET_SEND_BUFFER_SIZE)
        sock.connect((PacketEnum.SERVER, PacketEnum.PORT))
        cls.s = sock
        sock.settimeout(cls.read_timeout)

        return sock

    @classmethod
    def send_packet(cls, packet_type, ctx, datas=[]):
        import whatap.net.udp_thread
        try:
            if len(b''.join(cls.buffer_arr)) > PacketEnum.PACKET_BUFFER_SIZE:
                cls.send(packet_type, ctx)

            if not datas:
                return

            dout = DataOutputX()
            start_header_buffer_size = len(dout.buffer.getvalue())

            # header
            dout.writeByte(packet_type)
            dout.writeInt(PacketEnum.PACKET_VERSION)
            dout.writeInt(0)

            # body
            start_body_buffer_size = len(dout.buffer.getvalue())

            if ctx:
                dout.writeLong(ctx.id)
                dout.writeLong(ctx.start_time)
                dout.writeInt(ctx.elapsed)
                dout.writeLong(ctx.getCpuTime())
                dout.writeLong(ctx.getMemory())
                dout.writeInt(os.getpid())
                dout.writeLong(ctx.thread_id)

            diff = PacketEnum.PACKET_BUFFER_SIZE \
                   - len(b''.join(cls.buffer_arr)) - (PacketEnum.PACKET_BODY_REQUIRED_SIZE + 1)
            for data in datas:
                data = str(data)
                diff -= len(data)
                if diff < 0:
                    data = ' '
                    logging.debug('message too long.', extra={'id': 'WA999'},
                                  exc_info=False)
                dout.writeUTF(data)

            with cls.thread_lock:
                dout.writeToPos(
                    start_header_buffer_size + PacketEnum.PACKET_HEADER_LEN_POS,
                    len(dout.buffer.getvalue()) - start_body_buffer_size)

                cls.buffer_arr.append(dout.buffer.getvalue())

                if not ctx or packet_type == PacketTypeEnum.TX_START \
                        or packet_type == PacketTypeEnum.TX_END:
                    cls.send(packet_type, ctx)
        except Exception as e:
            logging.debug(e, extra={'id': 'WA913'}, exc_info=True)

    @classmethod
    def send(cls, packet_type, ctx):
        s = cls.s
        if not s:
            s = cls.udp()

        # for name, value in PacketTypeEnum.__dict__.items():
        #     if value == packet_type:
        #         print('pack_type: ', extra={'id': 'WA919'}, exc_info=True)

        try:
            s.sendall(b''.join(cls.buffer_arr))
        except ConnectionRefusedError as e:
            logging.debug(e, extra={'id': 'WA911'}, exc_info=True)
            cls.udp()
        except Exception as e:
            logging.debug(len(b''.join(cls.buffer_arr)))
            cls.buffer_arr.pop()
            logging.debug(len(b''.join(cls.buffer_arr)))
            logging.debug(e, extra={'id': 'WA912'}, exc_info=True)
            cls.send(packet_type, ctx)
            logging.debug('re send!')
        finally:
            cls.buffer_arr = []
            if packet_type == PacketTypeEnum.TX_END:
                TraceContextManager.end(ctx.thread_id)

    @classmethod
    def get(cls):
        from whatap.conf.configure import Configure as conf
        try:
            received = cls.s.recv(1024)
            if received:
                cls.handle(received.decode().split(','))
        except socket.error as serr:
            if serr.errno == errno.EAGAIN:
                conf.init(display=False)
            else:
                raise serr

    @classmethod
    def handle(cls, received):
        param_id, request, extra = tuple(received)
        param_id = int(param_id)
        thread_id = 0
        pid = 0
        if(extra != ''):
            extra_datas = extra.replace(' ', ', ').split(', ')
            thread_id, pid = TraceContextManager.parseThreadId(int(extra_datas[0]))

        data = ''
        if not param_id:
            # active stack pack
            datas = []
            data = extra.replace(' ', ', ')

            frame = sys._current_frames().get(thread_id)
            if not frame:
                return

            for stack in traceback.extract_stack(frame):
                line = stack[0]
                line_num = stack[1]
                method_name = stack[2]

                if line.find('/whatap/trace') > -1 or line.find('/threading.py') > -1:
                    continue
                data += '{} ({}:{})\n'.format(method_name, line, line_num)

            datas.append(data)

            cls.send_packet(PacketTypeEnum.ACTIVE_STACK, None, datas)
            stats = TraceContextManager.getActiveStats()
            datas = [','.join([str(x) for x in stats])]
            cls.send_packet(PacketTypeEnum.ACTIVE_STATS, None, datas)
        else:
            # param pack
            # format: "[packetType], [ctx], [datas: xxxx xxxx xxxx]"
            datas = [str(param_id), request]
            if param_id == ParamDef.MODULE_DEPENDENCY:
                import pip
                data = ', '.join(map(str, list(pip.get_installed_distributions())))
                datas.append(data)
            elif param_id == ParamDef.GET_ACTIVE_TRANSACTION_DETAIL:
                data = extra.replace(' ', ', ')

                frame = sys._current_frames().get(thread_id)
                if not frame:
                    return

                for stack in traceback.extract_stack(frame):
                    line = stack[0]
                    line_num = stack[1]
                    method_name = stack[2]

                    if line.find('whatap/trace') > -1:
                        continue
                    data += '{} ({}:{})\n'.format(method_name, line, line_num)

                datas.append(data)
            elif param_id == ParamDef.GET_ACTIVE_STATS:
                stats = TraceContextManager.getActiveStats()
                datas = [','.join([str(x) for x in stats])]
                cls.send_packet(PacketTypeEnum.ACTIVE_STATS, None, datas)
                return

            cls.send_packet(PacketTypeEnum.TX_PARAM, None, datas)
