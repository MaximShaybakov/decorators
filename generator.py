from itertools import chain
from decorators.decorator1 import logger_with_path


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


@logger_with_path(path='/home/maxim/git_projects/decors/logs/logs.log')
def one_list(ls: list) -> list:
    chain(*nested_list)
    res = [elem for elem in chain(*nested_list)]
    return res


def show():
    for obj in one_list():
        yield obj
        obj += 1


if __name__ == '__main__':
    for item in one_list(nested_list):
        print(item)