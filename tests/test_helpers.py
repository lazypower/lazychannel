import unittest
from mock import patch
from lazychannel import helpers


class TestHelpers(unittest.TestCase):

    def test_pexpand(self):
        px = helpers.pexpand
        self.assertEqual(px('~/tmp'), '/home/charles/tmp')

    @patch('lazychannel.helpers.os.path.exists')
    @patch('lazychannel.helpers.os.makedirs')
    def test_output_dir(self, osm, pem):
        pem.return_value = False
        helpers.output_dir('/tmp/foobar')
        osm.assert_called_with('/tmp/foobar')
