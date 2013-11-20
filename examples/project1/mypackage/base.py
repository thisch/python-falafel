import unittest
import logging
import types


class TestBase(unittest.TestCase):

    @classmethod
    def _createTests(cls, globals, **funcs):
        for name, func in funcs.items():
            newfunc = types.FunctionType(
                name=name, code=func.__code__,
                globals=globals, argdefs=func.__defaults__)
            setattr(cls, name, newfunc)

    def __init__(self, *args, **kwargs):
        super(TestBase, self).__init__(*args, **kwargs)
        self.created_files = []
        self.data = {}
        self.log = logging.getLogger("st")
        self.log.debug("testbase.__init__")
