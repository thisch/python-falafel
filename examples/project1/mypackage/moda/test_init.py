from os.path import splitext

from .. import TestBase


class DummyTest(TestBase):

    def _do_test_abc(self, x):
        base, ext = splitext(x)
        if ext.startswith('.'):
            ext = ext[1:]
        x = self.gen_filename(base, ext)
        if x:
            open(x, 'a').close()
            self.created_files.append(x)
            self.log.debug("added file %s", x)
        else:
            self.log.warning('no files were created because --log was not '
                             'specified in testrunner')
        self.log.error("test error")
        self.assertTrue(x)

    @classmethod
    def create_tests(cls):
        funcs = {}
        funcs['test_mysuper'] = lambda s, v="test.rst": s._do_test_abc(v)
        funcs['test_myfoo'] = lambda s, v="foobar.csv": s._do_test_abc(v)
        cls._create_tests(globals(), **funcs)
