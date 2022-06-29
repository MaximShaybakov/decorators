from decorators.decorator1 import logger, logger_with_path

# @logger
@logger_with_path(path='/home/maxim/git_projects/decors/logs/info_1.log')
def some_func(x: int, y: int):
    return f'{x} * {y} = {x * y}'


print(some_func(2, 3))