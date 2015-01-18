import unittest
import sys
from argparse import Namespace
from mock import patch, Mock, MagicMock
from lazychannel import generate

CFG_YML = """settings:
    dir: ~/Music
    limit: 15
    cache: "{}.cache"
youtube:
    osdir: 123123
"""


class TestConfig(unittest.TestCase):

    @patch("lazychannel.generate.os.makedirs")
    @patch('builtins.open' if sys.version_info > (3,) else '__builtin__.open')
    def test_create_config(self, mo, mkm):
        mo.return_value.__enter__ = lambda s: s
        mo.return_value.__exit__ = Mock()
        cfg = MagicMock()
        cfg.exists.return_value = False
        mkm.side_effect = Exception("Boom!")
        generate.log = MagicMock()

        generate.create_config('/tmp', cfg)
        mo.return_value.write.assert_called_with("        ArgoFoxCreativeCommons: UC56Qctnsu8wAyvzf4Yx6LIw\n")
        generate.log.debug.assert_called_once()

    @patch('builtins.open' if sys.version_info > (3,) else '__builtin__.open')
    def test_create_config_skips_when_exists(self, mo):
        mo.return_value.__enter__ = lambda s: s
        mo.return_value.__exit__ = Mock()
        cfg = MagicMock()
        cfg.exists.return_value = True

        generate.create_config('/tmp', cfg)
        mo.return_value.write.assert_not_called()

    @patch('lazychannel.generate.create_config')
    def test_main(self, ccm):
        args = Namespace(action='init', workspace='/tmp/foobar')
        generate.main(args, None)
        ccm.assert_called_once()

    def test_main_raises_exception_on_unknown_args(self):
        unknown = Namespace(foo='bar')
        self.assertRaises(Exception, generate.main, None, unknown)
