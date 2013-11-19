from .. import TestCase

# NOTE: this test is not run by the tester because the name of this file
# does not match the testpattern regex in TestLoader.discover


class TestBar(TestCase):
    def test_print(self):
        self.assertTrue(3+4 > 2)
