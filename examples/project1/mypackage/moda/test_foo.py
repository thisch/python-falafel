from __future__ import print_function

import unittest
import logging

from .. import TestBase
from ..decorators import interactive


class MyFooTest(TestBase):
    def comp(self, x):
        self.assertEqual(x, 4)

    def test_warning(self):
        self.log.warning("hello this is a test")
        self.log.error("blabla")
        self.log.debug("not shown in summary")

    def test_warning_andexception(self):
        self.log.warning("hello this is a test")
        self.log.error("blabla")
        self.log.debug("not shown in summary")
        self.assertTrue(False)

    def test_lala(self):
        self.log.info("TESTLOG in test_lala")
        print("MSG using 'print'")
        tlogger = logging.getLogger('pyspu')
        tlogger.info("LOGGING MSG FROM DIFFERENT LOGGER")
        import time
        time.sleep(1)
        self.log.debug("TESTLOG after log\nmultiline stuff\nmore lines")
        time.sleep(0.5)

        try:
            import numpy as np
        except ImportError:
            pass
        else:
            a = np.array([3, 2, 5])
            self.assertEqual(a.size, 4)

    @interactive
    def test_blub(self):
        a = 5
        name = raw_input("Enter your name")
        self.assertTrue(name != '')
        self.comp(a)


@unittest.skip("skip class")
class MySkipTest(TestBase):
    def comp(self, x):
        self.assertEqual(x, 4)

    def test_lu(self):
        self.log.info("TESTLOG in test_lala")
        import time
        time.sleep(1)
        self.log.debug("TESTLOG after log")
        time.sleep(0.5)

        try:
            import numpy as np
        except ImportError:
            pass
        else:
            a = np.array([3, 2, 5])
            self.assertEqual(a.size, 4)

    def test_bam(self):
        a = 5
        self.comp(a)
