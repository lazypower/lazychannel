import unittest
import sys
from mock import patch, Mock
from lazychannel import sync

CFG_YML = """settings:
    dir: ~/Music
    limit: 15
youtube:
    osdir: 123123
"""

class TestSync(unittest.TestCase):

    def test_something(self):
        pass
