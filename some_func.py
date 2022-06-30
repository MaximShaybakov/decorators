import os.path
from decorators.decorator1 import logger, logger_with_path

path = os.path.abspath('generator.py')

# @logger
@logger_with_path(path=f'{os.path.dirname(path)}/logs/info_1.log')
def some_func(x: int, y: int):
    return f'{x} * {y} = {x * y}'


print(some_func(2, 3))