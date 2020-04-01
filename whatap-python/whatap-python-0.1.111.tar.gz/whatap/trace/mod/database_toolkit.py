from whatap.net.packet_type_enum import PacketTypeEnum
from whatap.net.udp_session import UdpSession
from whatap.trace.mod.application_wsgi import trace_handler, interceptor_db_execute
from whatap.util.date_util import DateUtil
from whatap.trace.trace_context_manager import TraceContextManager

def instrument_sqlalchemy(module):
    def wrapper(fn):
        @trace_handler(fn)
        def trace(*args, **kwargs):
            ctx = TraceContextManager.getLocalContext()
            
            start_time = DateUtil.nowSystem()
            ctx.start_time = start_time
            
            text = args[0].bind.url.__to_string__().replace('***', '')
            ctx.lctx['dbc'] = text
            
            datas = [' ', ' ', 'DB SESSION INFO: ' + text]
            ctx.elapsed = DateUtil.nowSystem() - start_time
            UdpSession.send_packet(PacketTypeEnum.TX_MSG, ctx, datas)
            
            callback = fn(*args, **kwargs)
            return callback
        
        return trace
    
    module.Session.get_bind = wrapper(module.Session.get_bind)

def addQuote(arg_dict):
    quoted_dict = dict()

    for k, v in arg_dict.items():
        if isinstance(v, str):
            quoted_dict[k] = "'" + v.replace("'", "\\'") + "'"
        else:
            quoted_dict[k] = v

    return quoted_dict

def instrument_sqlalchemy_engine(module):
    def wrapper(fn):
        @trace_handler(fn)
        def trace(*args, **kwargs):
            # print('instrument_sqlalchemy_engine step -1')
            ctx = TraceContextManager.getLocalContext()
            # print('instrument_sqlalchemy_engine CTX:', ctx)
            cursor = args[1]
            query = None
            if len(args) > 3 and type(args[3]) == dict and args[3]:
                try:
                    query = args[2] % addQuote(args[3])
                except Exception as e:
                    pass
            # print('instrument_sqlalchemy_engine 2:', query)
            try:
                if not query:
                    query = args[2].decode()
            except Exception as e:
                query = str(args[2])
            # print('instrument_sqlalchemy_engine 3:', query)
            if not query or ctx.active_sqlhash:
                return fn(*args, **kwargs)

            start_time = DateUtil.nowSystem()
            ctx.start_time = start_time
            ctx.active_sqlhash = query
            # print('instrument_sqlalchemy_engine 4')
            try:
                callback = fn(*args, **kwargs)
                # print('instrument_sqlalchemy_engine 5')
                return callback
            except Exception as e:
                interceptor_step_error(e)
            finally:
                # print('instrument_sqlalchemy_engine 6')
                datas = [ctx.lctx.get('dbc', ''), query]
                ctx.elapsed = DateUtil.nowSystem() - start_time
                # print('instrument_sqlalchemy_engine 6.1', datas)
                UdpSession.send_packet(PacketTypeEnum.TX_SQL, ctx,
                                       datas)
                # print('instrument_sqlalchemy_engine 7')
                count = cursor.rowcount
                # print('instrument_sqlalchemy_engine 8')
                if count > -1:
                    desc = '{0}: {1}'.format('Fetch count', count)
                    datas = [' ', ' ', desc]
                    ctx.elapsed = 0
                    UdpSession.send_packet(PacketTypeEnum.TX_MSG, ctx, datas)
                ctx.active_sqlhash = 0
                # print('instrument_sqlalchemy_engine 9')

        return trace

    # print('database_toolkit.instrument_sqlalchemy_engine step -1')
    if hasattr(module, 'DefaultDialect') and hasattr(module.DefaultDialect, 'do_execute'):
        # print('database_toolkit.instrument_sqlalchemy_engine step -2')
        module.DefaultDialect.do_execute = wrapper(module.DefaultDialect.do_execute)
        module.DefaultDialect.do_executemany = wrapper(module.DefaultDialect.do_executemany)
        module.DefaultDialect.do_execute_no_params = wrapper(module.DefaultDialect.do_execute_no_params)
        # print('database_toolkit.instrument_sqlalchemy_engine step -3')