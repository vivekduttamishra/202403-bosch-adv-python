from functools import wraps

def error_mapper(ex_type, message="Error", error_status=404, key_name='id'):
    def target_wrapper( route_function):
        @wraps(route_function)
        def wrapper(*args, **kwargs):
            print(f'wrapper to {route_function.__name__}:{args=},{kwargs=}')
            try:
                return route_function(*args, **kwargs)
            except ex_type as e:                
                return {
                    "error": message,
                    "error_status": error_status,
                    "id": kwargs.get(key_name,"n/a")
                }, error_status
        return wrapper
    return target_wrapper


