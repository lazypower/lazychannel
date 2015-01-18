import unittest
import yaml
from argparse import Namespace
from mock import patch
from lazychannel import sync

CFG_YML = """settings:
    dir: ~/Music
    limit: 15
    cache: "{}.cache"
channels:
    youtube:
        osdir: 123123
"""


class TestSync(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.args = Namespace(workspace='/home/foo/.bar', d='/home/foo/Music')
        cls.config = yaml.safe_load(CFG_YML)

    @patch('lazychannel.config.config.load_config')
    @patch('lazychannel.sync.output_dir')
    def test_main(self, sm, lcm):
        print(self.config)
        lcm.return_value = self.config
        sync.main(self.args, None)

    def test_main_raises_exception(self):
        self.assertRaises(Exception, sync.main, self.args, self.args)
