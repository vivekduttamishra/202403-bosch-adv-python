from functools import wraps

def error_mapper(ex_type, message="Error", error_status=404):
    def target_wrapper( route_function):
        @wraps(route_function)
        def wrapper(*args, **kwargs):
            try:
                return route_function(*args, **kwargs)
            except ex_type as e:                
                return {
                    "error": message,
                    "error_status": error_status,
                    "id": args[0] if len(args) else "n/a"
                }, error_status
        return wrapper
    return target_wrapper


