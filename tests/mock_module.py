import sys

from types import ModuleType
from unittest.mock import MagicMock

class MockModule(ModuleType):
    '''
    A class of module which squats on sys.modules for a given module name.
    It returns a MagicMock for every attribute, which allows arbitrary imports
    of the form `from fake_module import Foo`.
    '''

    def __init__(self, name):
        '''
        After creating an instance of this module, importing `name` will load
        that instance.
        '''
        sys.modules[name] = self
        super().__init__(name)

    def __getattr__(self, name):
        return MagicMock(self.__name__ + '.' + name)
