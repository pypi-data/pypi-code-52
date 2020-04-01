import traceback

import sys

from whatap.conf.configure import Configure as conf
from whatap.net.packet_type_enum import PacketTypeEnum
from whatap.net.udp_session import UdpSession
from whatap.trace.trace_context import TraceContext
from whatap.trace.trace_context_manager import TraceContextManager
from whatap.util.date_util import DateUtil
from whatap.util.userid_util import UseridUtil as userid_util
from functools import wraps
from whatap import logging
import re

from whatap.util.hexa32 import Hexa32

import traceback, threading

def isEventlet():
    greenlet = sys.modules.get('greenlet')

    if greenlet:
        current = greenlet.getcurrent()
        if current is not None and current.parent:
            print('thread:',threading.get_ident(),'greenlet:', id(current.parent))
            traceback.print_stack()
            return True
    else:
        return False

def trace_handler(fn, start=False):
    def handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # if isEventlet():
            #     print("trace_handler: greenlet found")
            # else:
            #     print("trace_handler: greenlet not found")
            ctx = TraceContextManager.getLocalContext()
            # print("trace_handler ctx:", ctx)
            if not start and not ctx:
                return fn(*args, **kwargs)
            
            # check raise step error
            if ctx and ctx.error_step:
                end_interceptor(ctx=ctx)
                raise Exception(ctx.error_step)
            
            try:
                callback = func(*args, **kwargs)
            except Exception as e:
                logging.debug(e, extra={'id': 'WA917'}, exc_info=True)
                print(e, dict(extra={'id': 'WA917'}, exc_info=True))
                return fn(*args, **kwargs)
            else:
                return callback
        
        return wrapper
    
    return handler


def start_interceptor(ctx):
    if conf.dev:
        logging.debug('start transaction id(seq): {}'.format(ctx.id),
                      extra={'id': 'WA111'})
        print('start transaction id(seq): {}'.format(ctx.id),dict(extra={'id': 'WA111'}))
    
    start_time = DateUtil.nowSystem()
    ctx.start_time = start_time
    
    datas = [ctx.host,
             ctx.service_name,
             ctx.remoteIp,
             ctx.userAgentString,
             ctx.referer,
             ctx.userid,
             ctx.isStaticContents
             ]
    # print("start_interceptor txid:", ctx.id)
    UdpSession.send_packet(PacketTypeEnum.TX_START, ctx, datas)
    
    return ctx

def end_interceptor(thread_id=None, ctx= None):
    if not ctx:
        ctx = TraceContextManager.getContext(
            thread_id) if thread_id else TraceContextManager.getLocalContext()
    if not ctx:
        return

    if conf.dev:
        logging.debug('end   transaction id(seq): {}'.format(ctx.id),
                      extra={'id': 'WA112'})
        print('end   transaction id(seq): {}'.format(ctx.id),
                      dict(extra={'id': 'WA112'}))

    start_time = DateUtil.nowSystem()
    ctx.start_time = start_time

    datas = [ctx.host, ctx.service_name, ctx.mtid, ctx.mdepth, ctx.mcaller_txid,
             ctx.mcaller_pcode, ctx.mcaller_spec, ctx.mcaller_url]
    ctx.elapsed = DateUtil.nowSystem() - start_time

    UdpSession.send_packet(PacketTypeEnum.TX_END, ctx, datas)

def interceptor(rn_environ, *args, **kwargs):
    if not isinstance(rn_environ, tuple):
        rn_environ = (rn_environ, args[1])
    fn, environ = rn_environ
    
    ctx = TraceContext()
    ctx.host = environ.get('HTTP_HOST', '').split(':')[0]
    ctx.service_name = environ.get('PATH_INFO', '')

    ctx.remoteIp = userid_util.getRemoteAddr(args)

    ctx.userAgentString = environ.get('HTTP_USER_AGENT', '')
    ctx.referer = environ.get('HTTP_REFERER''', '')

    if conf.trace_user_enabled:
        if conf.trace_user_using_ip:
            ctx.userid = userid_util.getRemoteAddr(args)
        else:
            ctx.userid, ctx._rawuserid = userid_util.getUserId(args, ctx.remoteIp)

    mstt = environ.get('HTTP_{}'.format(
        conf._trace_mtrace_caller_key.upper().replace('-', '_')), '')
    
    if mstt:
        ctx.setTransfer(mstt)
        if conf.stat_mtrace_enabled:
            val = environ.get('HTTP_{}'.format(
                conf._trace_mtrace_info_key.upper().replace('-', '_')), '')
            if val and len(val):
                ctx.setTransferInfo(val)
            pass

        myid = environ.get('HTTP_{}'.format(
            conf._trace_mtrace_callee_key.upper().replace('-', '_')), '')
        if myid:
            ctx.setTxid(myid)
    start_interceptor(ctx)
    
    callback = fn(*args, **kwargs)

    if ctx:
        query_string = environ.get('QUERY_STRING', '')
        if query_string:
            ctx.service_name += '?{}'.format(query_string)

        if ctx.service_name.find('.') > -1 and ctx.service_name.split('.')[
            1] in conf.web_static_content_extensions:
            ctx.isStaticContents = 'true'

        if getattr(callback, 'status_code', None):
            status_code = callback.status_code
            errors = [callback.reason_phrase, callback.__class__.__name__]
            interceptor_error(status_code, errors)
        
        if conf.profile_http_header_enabled:
            keys = []
            for key, value in environ.items():
                if key.startswith('HTTP_'):
                    keys.append(key)
            keys.sort()
            
            text = ''
            for key in keys:
                text += '{}={}\n'.format(key.split('HTTP_')[1].lower(),
                                         environ[key])
            
            datas = ['HTTP-HEADERS', 'HTTP-HEADERS', text]
            ctx.start_time = DateUtil.nowSystem()
            UdpSession.send_packet(PacketTypeEnum.TX_MSG, ctx, datas)
        end_interceptor(ctx=ctx)
    return callback


def interceptor_error(status_code, errors):
    print('error', status_code, errors)
    ctx = TraceContextManager.getLocalContext()
    ctx.status = int(status_code / 100)
    if ctx.status >= 4 and not ctx.error:
        ctx.error = 1
        
        error = ''
        frame = sys._current_frames().get(ctx.thread.ident)
        if not frame:
            return
        
        for stack in traceback.extract_stack(frame):
            line = stack[0]
            line_num = stack[1]
            method_name = stack[2]

            if line.find('/whatap/trace') > -1 or line.find(
                    '/threading.py') > -1:
                continue
            error += '{} ({}:{})\n'.format(method_name, line, line_num)
        
        errors.append(error)
        
        # errors.append(''.join(traceback.format_list(traceback.extract_stack(sys._current_frames()[ctx.thread.ident]))))
        UdpSession.send_packet(PacketTypeEnum.TX_ERROR, ctx, errors)


def interceptor_step_error(e):
    print('interceptor_step_error', e)
    ctx = TraceContextManager.getLocalContext()
    ctx.error_step = e
    if not ctx.error:
        ctx.error = 1
    
    errors = []
    errors.append(e.__class__.__name__)
    errors.append(str(e.args[0]))
    
    error = ''
    frame = sys._current_frames().get(ctx.thread.ident)
    if not frame:
        return
    
    for stack in traceback.extract_stack(frame):
        line = stack[0]
        line_num = stack[1]
        method_name = stack[2]
        
        if line.find('/whatap/trace') > -1 or line.find('/threading.py') > -1:
            continue
        error += '{} ({}:{})\n'.format(method_name,line, line_num)
    
    errors.append(error)
    # errors.append(''.join(traceback.format_list(traceback.extract_stack(sys._current_frames()[ctx.thread.ident]))))
    UdpSession.send_packet(PacketTypeEnum.TX_ERROR, ctx, errors)

    if conf.profile_exception_stack:
        desc = '\n'.join(errors)
        datas = [' ', ' ', desc]
        ctx.start_time = DateUtil.nowSystem()
        UdpSession.send_packet(PacketTypeEnum.TX_MSG, ctx, datas)

def interceptor_httpc_request(fn, httpc_url, *args, **kwargs):
    ctx = TraceContextManager.getLocalContext()
    if not ctx or ctx.active_httpc_hash:
        return fn(*args, **kwargs)

    param = None
    method = None
    if httpc_url.find('?') > -1:
        httpc_url, param = httpc_url.split('?')

    start_time = DateUtil.nowSystem()
    ctx.start_time = start_time
    ctx.httpc_url = httpc_url
    ctx.active_httpc_hash = ctx.httpc_url
    
    try:
        callback = fn(*args, **kwargs)
        return callback
    except Exception as e:
        interceptor_step_error(e)
        print('interceptor_httpc_request', e)
    finally:
        datas = [ctx.httpc_url, ctx.mcallee]
        ctx.elapsed = DateUtil.nowSystem() - start_time
        UdpSession.send_packet(PacketTypeEnum.TX_HTTPC, ctx, datas)

        if conf.profile_http_parameter_enabled:
            if type(args[1]) == dict:
                param = (args[1].body if 'body' in args[1] else args[1]) or param
                method = args[1].method if 'method' in args[1] else args[1]

            if param:
                datas = ['HTTP-PARAMETERS', method, param]
                ctx.start_time = DateUtil.nowSystem()
                UdpSession.send_packet(PacketTypeEnum.TX_SECURE_MSG, ctx, datas)

        ctx.active_httpc_hash = 0
        ctx.httpc_url = None

def interceptor_sock_connect(fn, *args, **kwargs):
    ctx = TraceContextManager.getLocalContext()
    if not ctx :
        return fn(*args, **kwargs)

    try:
        ctx.socket_connecting = True
        callback = fn(*args, **kwargs)
        return callback
    except Exception as e:
        interceptor_step_error(e)
        print('interceptor_sock_connect', e)
    finally:
        ctx.socket_connecting = False

def interceptor_db_con(fn, db_type, *args, **kwargs):
    ctx = TraceContextManager.getLocalContext()
    if ctx.db_opening:
        return fn(*args, **kwargs)
    
    start_time = DateUtil.nowSystem()
    ctx.start_time = start_time

    ctx.db_opening = True
    try:
        callback = fn(*args, **kwargs)
    finally:

        ctx.db_opening = False

    if not kwargs:
        kwargs = dict(
            x.split('=') for x in re.sub(r'\s*=\s*', '=', args[0]).split())
    
    text = '{}://'.format(db_type)
    text += kwargs.get('user')
    text += "@"
    text += kwargs.get('host')
    text += '/'
    text += kwargs.get('database', kwargs.get('db', kwargs.get('dbname')))
    ctx.active_dbc = text
    ctx.lctx['dbc'] = text
    
    ctx.active_dbc = 0

    datas = [text]
    ctx.elapsed = DateUtil.nowSystem() - start_time
    UdpSession.send_packet(PacketTypeEnum.TX_DB_CONN, ctx, datas)
    
    return callback

def addQuote(arg_dict):
    quoted_dict = dict()

    for k, v in arg_dict.items():
        if isinstance(v, str):
            quoted_dict[k] = "'" + v.replace("'", "\\'") + "'"
        else:
            quoted_dict[k] = v

    return quoted_dict

def interceptor_db_execute(fn, *args, **kwargs):
    # print('interceptor_db_execute step -1')
    ctx = TraceContextManager.getLocalContext()
    # print('interceptor_db_execute step -2 ctx:', ctx)
    self = args[0]
    query = None
    if len(args) > 2 and type(args[2]) == dict and args[2]:
        try:
            query = args[1] % addQuote(args[2])
        except Exception as e:
            pass
    try:
        if not query:
            query = args[1].decode()
    except Exception as e:
        query = args[1]
    #print('interceptor_db_execute step -3', query)
    if not query or ctx.active_sqlhash:
        #print('interceptor_db_execute step -3.1', ctx.active_sqlhash)
        return fn(*args, **kwargs)


    # print('interceptor_db_execute step -4')
    start_time = DateUtil.nowSystem()
    ctx.start_time = start_time
    ctx.active_sqlhash = query
    # print('interceptor_db_execute step -5')
    try:
        callback = fn(*args, **kwargs)
        # print('interceptor_db_execute step -6')
        return callback
    except Exception as e:

        interceptor_step_error(e)
    finally:
        # print('interceptor_db_execute step -7 txid:', ctx.id)
        datas = [ctx.lctx.get('dbc', ''), query]
        ctx.elapsed = DateUtil.nowSystem() - start_time
        UdpSession.send_packet(PacketTypeEnum.TX_SQL, ctx,
                               datas)
        # print('interceptor_db_execute step -8')
        count = self.rowcount
        # print('interceptor_db_execute step -9', count)
        if count > -1:
            desc = '{0}: {1}'.format('Fetch count', count)
            datas = [' ', ' ', desc]
            ctx.elapsed = 0
            UdpSession.send_packet(PacketTypeEnum.TX_MSG, ctx, datas)
        
        ctx.active_sqlhash = 0
        # print('interceptor_db_execute step -10')

def interceptor_db_close(fn, *args, **kwargs):
    ctx = TraceContextManager.getLocalContext()
    ctx.db_opening = False
    
    if not conf.profile_dbc_close:
        return fn(*args, **kwargs)
    
    start_time = DateUtil.nowSystem()
    ctx.start_time = start_time
    
    callback = fn(*args, **kwargs)
    
    text = 'DB: Close Connection.'
    datas = [' ', ' ', text]
    ctx.elapsed = DateUtil.nowSystem() - start_time
    UdpSession.send_packet(PacketTypeEnum.TX_MSG, ctx, datas)
    return callback


check_seq = 1


def inter_tx_trace_auto_on(ctx):
    try:
        if isinstance(conf.mtrace_rate, str):
            conf.mtrace_rate = int(conf.mtrace_rate)
    except ValueError:
        conf.mtrace_rate = 0
    finally:
        if conf.mtrace_rate <= 0 or ctx.httpc_checked or ctx.mtid != 0:
            return
        
        ctx.httpc_checked = True
        
        try:
            inter_tx_trace_auto_on.check_seq += 1
        except AttributeError:
            inter_tx_trace_auto_on.check_seq = 1
        finally:
            check_seq = inter_tx_trace_auto_on.check_seq
            
            rate = int(conf.mtrace_rate / 10)
            if rate == 10:
                ctx.mtid = TraceContextManager.getId()
            elif rate == 9:
                if check_seq % 10 != 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 8:
                if check_seq % 5 != 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 7:
                if check_seq % 4 != 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 6:
                if check_seq % 3 != 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 5:
                if check_seq % 2 == 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 4:
                if check_seq % 3 == 0 or check_seq % 5 == 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 3:
                if check_seq % 4 == 0 or check_seq % 5 == 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 2:
                if check_seq % 5 == 0:
                    ctx.mtid = TraceContextManager.getId()
            elif rate == 1:
                if check_seq % 10 == 0:
                    ctx.mtid = TraceContextManager.getId()


def transfer(headers):
    ctx = TraceContextManager.getLocalContext()
    
    if not ctx.mtid:
        inter_tx_trace_auto_on(ctx)
    
    if ctx.mtid:
        headers[conf._trace_mtrace_caller_key] = ctx.transfer()
        if conf.stat_mtrace_enabled:
            headers[conf._trace_mtrace_info_key] = ctx.transferInfo()

        ctx.mcallee = TraceContextManager.getId()
        headers[conf._trace_mtrace_callee_key] = Hexa32.toString32(ctx.mcallee)
    return headers
