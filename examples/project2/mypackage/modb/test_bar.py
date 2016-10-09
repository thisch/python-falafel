import logging

from .. import TestBase

LOGGER = logging.getLogger(__name__)


class TestBar(TestBase):
    def test_print(self):

        LOGGER.info("one of the tests in test_bar.py\n" +
                    '\n'.join([str(x) for x in range(10)]))
        self.assertTrue(3+4 > 2)
        LOGGER.debug("looks good")
