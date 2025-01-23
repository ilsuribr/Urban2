import inspect
import math
from pprint import pprint


class MyClass():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'привет {self.name}')


def introspection_info(obj):
    result = {}

    result['type'] = type(obj)

    try:
        result['attributes'] = vars(obj)
    except TypeError:
        result['attributes'] = dir(obj)

    result['methods'] = inspect.getmembers(obj, predicate=inspect.ismethod)
    result['module'] = inspect.getmodule(obj)

    try:
        result['__name__'] = obj.__name__
    except AttributeError:
        result['__name__'] = None

    result['callalbe'] = callable(obj)
    result['isbuiltin'] = inspect.isbuiltin(obj)

    return result

obj1 = math
obj2 = MyClass('Антон')
obj3 = 42
obj4 = 'строка'
number_info = introspection_info(obj4)
pprint(number_info)
