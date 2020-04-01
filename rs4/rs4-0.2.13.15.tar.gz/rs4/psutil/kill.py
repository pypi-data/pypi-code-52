import os
import signal, psutil

def thread (thread):
    import ctypes    
    if not thread.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        # raise ValueError ("nonexistent thread id")
        pass
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError ("PyThreadState_SetAsyncExc failed")

def process (p, sig = signal.SIGTERM):
    if isinstance (p, int):
        # resolve to process
        try:
            p = psutil.Process (p)        
        except psutil.NoSuchProcess:
            return    
    p.send_signal (sig)

# utils -------------------------------------------
def child_processes (parent_pid = os.getpid (), sig = signal.SIGTERM):    
    try:
        parent = psutil.Process (parent_pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children (recursive = True)
    for process in children:
        process.send_signal (sig)