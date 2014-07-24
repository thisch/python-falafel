from .. import TestBase


class TestBar(TestBase):
    def test_print(self):

        self.log.info("one of the tests in test_bar.py\n" +
                      '\n'.join([str(x) for x in range(10)]))
        self.assertTrue(3+4 > 2)
        self.log.debug("looks good")
