from decorator1 import logger

@logger
def some_func(x: int, y: int):
    return x * y


some_func(2, 3)