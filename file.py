from decorator1 import logger

@logger
def some_func(x: int, y: int):
    return f'{x} * {y} = {x * y}'


print(some_func(2, 3))