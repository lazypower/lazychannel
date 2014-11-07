import unittest
import sys
from mock import patch, Mock
from lazychannel import generate

CFG_YML = """settings:
    dir: ~/Music
    limit: 15
youtube:
    osdir: 123123
"""

class TestConfig(unittest.TestCase):

    @patch(lazychannel.config.config.exists)
    @patch(lazychannel.generate.os.makedirs)
    @patch('builtins.open' if sys.version_info > (3,) else '__builtin__.open')
    def test_create_config(self, mo, mkm, exm):
        mo.return_value.__enter__ = lambda s: s
        mo.return_value.__exit__ = Mock()
        exm.return_value = False
        mo.return_value.write.assert_called_with("youtube:\n")
        generate.create_config('/tmp')
