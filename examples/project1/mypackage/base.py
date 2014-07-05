from os.path import join
import unittest
import logging
import types


class TestBase(unittest.TestCase):

    @classmethod
    def _create_tests(cls, globals, **funcs):
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

    def gen_filename(self, postfix, extension):
        if not hasattr(self, '_logdir'):
            # _logdir gets set by the falafel testrunner. More precisely by
            # the ResultHandler class
            return None
        fname = "%s_%s%s.%s" % (self.__class__.__name__,
                                self._testMethodName,
                                "_%s" % postfix if postfix else "",
                                extension)
        fname = join(self._logdir, fname)
        return fname
