from .. import TestBase


class DummyTest(TestBase):

    def _do_test_abc(self, x):
        self.created_files.append(x)
        self.assertTrue(x)

    @classmethod
    def createTests(cls):
        funcs = {}
        funcs['test_mysuper'] = lambda s, v="blub": s._do_test_abc(v)
        funcs['test_myfoo'] = lambda s, v=False: s._do_test_abc(v)
        cls._createTests(globals(), **funcs)
