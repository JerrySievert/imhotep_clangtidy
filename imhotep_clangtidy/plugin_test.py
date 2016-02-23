from unittest import TestCase
import mock
from .plugin import ClangTidy


class ClangTidyTest(TestCase):
    def test_command_returns_airbnb_if_no_config(self):
        plugin = ClangTidy(None)
        with mock.patch('os.path') as mock_op:
            mock_op.join.return_value = '/tmp/foo.cpp'
            mock_op.exists.return_value = False
            cmd = plugin.get_command('/tmp')
            self.assertEqual('clang-tidy', cmd)
