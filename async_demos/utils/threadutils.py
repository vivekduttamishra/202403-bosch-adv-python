import threading
from functools import wraps

class Task(threading.Thread):
    def __init__(self,fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.start()
        self._result=None

    def run(self):
        self._result = self.fn(*self.args, **self.kwargs)

    @property
    def result(self):
        self.join()
        return self._result

    
def asynchronous(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        task = Task(fn, *args, **kwargs)
        return task

    #we pass original funciton as sync property
    wrapper.sync=fn # if you really want to run your function synchronously


    return wrapper
        

