"""Tests for rsync_snap"""
import unittest
import subprocess
import sys
#  from rsync_snap import (PROG_NAME, PROG_DESC, BACKUP_PROFILE_HELP,
#  get_args)
#  from rsync_snap import
from rsync_snap import (
    PROG_NAME,
    BACKUP_PROFILE_META,
    BACKUP_PROFILE_HELP,
    get_args,
)


class ArgParseSourceTests(unittest.TestCase):
    """Tests involving the use of argument parsing"""
    # Below is the expected output#
    """usage: rsync_snap.py [-h] BACKUP_PROFILE
rsync_snap.py: error: the following arguments are required: BACKUP_PROFILE"""

    def test_no_arg(self):
        """Test for printing the right response for running without args"""
        no_arg_output = subprocess.run('./rsync_snap.py',
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
        no_arg_output = no_arg_output.stderr.decode('UTF-8')
        self.assertIn('usage:', no_arg_output)
        self.assertIn('-h', no_arg_output)
        self.assertIn('error', no_arg_output)
        self.assertIn(BACKUP_PROFILE_META, no_arg_output)

    def test_h_for_help(self):
        """Test that entering '-h' brings up help output"""
        h_arg_output = subprocess.run('./rsync_snap.py -h'.split(),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        h_arg_output = h_arg_output.stdout.decode('UTF-8')
        expected_outputs = [
            'usage', PROG_NAME, '-h', 'arguments:', BACKUP_PROFILE_HELP]
        for substring in expected_outputs:
            self.assertIn(substring, h_arg_output)

    def test_that_h_arg_equals_help_arg(self):
        """Test that '-h' as an arg does the same thing as '--help'"""
        h_arg_output = subprocess.run('./rsync_snap.py -h'.split(),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        h_arg_output = h_arg_output.stdout.decode('UTF-8')
        help_arg_output = subprocess.run('./rsync_snap.py -h'.split(),
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
        help_arg_output = help_arg_output.stdout.decode('UTF-8')
        self.assertEqual(h_arg_output, help_arg_output)

    def test_profilename_given_valid_arg(self): # pylint: disable=invalid-name
        """Tests entering a valid profile name stores it correctly as
        PROFILE_NAME"""
        expected_profile = 'abc-123_XYZ'
        sys.argv[1:] = [expected_profile]
        args = get_args()
        self.assertEqual(expected_profile, args.backup_profile)

    def test_invalid_profile_name_fails(self):
        """Tests that entering any character but alphanumeric or '-_' causes:
            - an exit code
            - an error message mentioning invalid character use in profile
            - a message that detailing valid characters to use"""
        invalid_string = 'abc!./,)(#@'
        h_arg_output = subprocess.run(['./rsync_snap.py', invalid_string],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        h_arg_err = h_arg_output.stderr.decode('UTF-8')
        h_arg_output = h_arg_output.stdout.decode('UTF-8')
        self.assertEqual('', h_arg_output)
