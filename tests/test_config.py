import unittest
import sys
from mock import patch, Mock
from lazychannel.config import config

CFG_YML = """settings:
    dir: ~/Music
    limit: 15
youtube:
    osdir: 123123
"""

class TestConfig(unittest.TestCase):

    def test_attributes(self):
        c = config('/tmp')
        self.assertEqual(c.config, '/tmp/config.yaml')

    def test_dir(self):
        c = config('/tmp')
        self.assertEqual(c.dir(), '/tmp')

    @patch('os.path.exists')
    def test_exists(self, exmock):
        exmock.return_value = True
        c = config('/tmp')
        self.assertEqual(c.exists(), True)
        exmock.return_value = False
        self.assertEqual(c.exists(), False)

    @patch('lazychannel.config.config.exists')
    @patch('builtins.open' if sys.version_info > (3,) else '__builtin__.open')
    def test_load_config(self, mo, exmock):
        exmock.return_value = True
        mo.return_value.__enter__ = lambda s: s
        mo.return_value.__exit__ = Mock()
        mo.return_value.read.return_value = CFG_YML

        c = config('/tmp').load_config()
        self.assertEqual(c['settings']['limit'], 15)
