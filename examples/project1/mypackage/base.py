import unittest
import logging

class TestBase(unittest.TestCase):

    @classmethod
    def _createTests(cls, globals, **funcs):
        import new
        for name, func in funcs.iteritems():
            setattr(cls, name,
                    new.instancemethod(new.function(
                        name=name, code=func.__code__, globals=globals,
                        argdefs=func.__defaults__), None, cls))

    def __init__(self, *args, **kwargs):
        super(TestBase, self).__init__(*args, **kwargs)
        self.created_files = []
        self.data = {}
        self.log = logging.getLogger("st")
        self.log.debug("testbase.__init__")
