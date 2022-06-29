from datetime import datetime
import os

def logger(old_func):

    def new_func(*args, **kwargs):
        func_call = datetime.now()
        res = old_func(*args, **kwargs)
        with open('info.log', 'a+') as file:
            info = file.writelines(f'[datetime: {func_call},\nname func: {old_func.__name__},\narguments: {args} and {kwargs}]\n')
        return res

    return new_func