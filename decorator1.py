from datetime import datetime
from functools import wraps
import os

def logger(old_func):

    @wraps(old_func)
    def new_func(*args, **kwargs):
        func_call = datetime.now()
        res = old_func(*args, **kwargs)
        with open('info.log', 'a+') as file:
            info = file.writelines(f'''[datetime: {func_call},\nname func: {old_func.__name__},\narguments: {args} and {kwargs},\nwas returned: {res}]\n''')
        return res

    return new_func

def path_to_log(path):

    def logger_with_path(old_func):

        @wraps(old_func)
        def new_func(*args, **kwargs):
            nonlocal path
            # path =
            result = old_func(*args, **kwargs)

            return result

        return new_func

    return path_to_log