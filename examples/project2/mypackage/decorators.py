import unittest
import os

interactive = unittest.skipIf(
    not os.getenv('INTERACTIVE_TESTS'), 'interactive test')
