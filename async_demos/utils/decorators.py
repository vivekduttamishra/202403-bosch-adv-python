import time
from functools import wraps

def performance(target):
    @wraps(target)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = target(*args, **kwargs)
            end_time = time.time()
            return result
        finally:
            end_time = time.time()
            print(f"Time taken {target.__name__}: {end_time - start_time} seconds")
    return wrapper


def delay(seconds):

    def target_wrapper(target):
        @wraps(target)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return target(*args, **kwargs)
        return wrapper
    return target_wrapper


def log_call(target):
    @wraps(target)
    def wrapper(*args, **kwargs):
        print(f"Calling {target.__name__}")
        result = target(*args, **kwargs)
        print(f"Called {target.__name__}")
        return result
    return wrapper 
