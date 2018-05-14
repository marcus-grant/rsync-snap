#!/usr/bin/env python3
"""Tests for rsync_snap"""
import unittest
import subprocess
import sys
import configparser
import os

#  from rsync_snap import (PROG_NAME, PROG_DESC, BACKUP_PROFILE_HELP,
#  get_args)
#  from rsync_snap import
from rsync_snap import (
    PROG_NAME,
    BACKUP_PROFILE_META,
    BACKUP_PROFILE_HELP,
    PROFILE_NAME_ERR,
    get_args,
    is_valid_profile_name,
    parse_config,
)


class TestArgParsing(unittest.TestCase):
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

    def test_is_valid_profile_name_valid(self):  # pylint: disable=invalid-name
        """Test that is_valid_profile_name returns a profile name
        when valid characters are given to it"""
        expected_profile = 'abc-123_XYZ'
        sys.argv[1:] = [expected_profile]
        args = get_args()
        self.assertEqual(expected_profile,
                         is_valid_profile_name(args.backup_profile))

    def test_is_valid_profile_name_invalid(self):
        """Test that is_valid_profile_name exits with an error message
        and the right error message when invalid characters are used"""
        given_profiles = [
            'a!', 'a@', 'a#', 'a$', 'a%', 'a^', 'a*',
            'a+', 'a=', 'a:', 'a,', 'a.', 'a?',
        ]
        for profile in given_profiles:
            with self.assertRaises(SystemExit) as exit_case:
                is_valid_profile_name(profile)
            self.assertEqual(exit_case.exception.code, PROFILE_NAME_ERR)

    def test_invalid_profile_name_fail(self):
        """Test that when script is given invalid profile,
        it fails with the right message"""
        given_profiles = [
            'XYZ!', 'XYZ@', 'XYZ#', 'XYZ$', 'XYZ%', 'XYZ^', 'XYZ*',
            'XYZ+', 'XYZ=', 'XYZ:', 'XYZ,', 'XYZ.', 'XYZ?',
        ]
        for profile in given_profiles:
            invalid_output = subprocess.run(['./rsync_snap.py', profile],
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
            invalid_err = invalid_output.stderr.decode('UTF-8')
            invalid_output = invalid_output.stdout.decode('UTF-8')
            # check that stdout is empty
            self.assertEqual(invalid_output, '')
            self.assertIn(PROFILE_NAME_ERR, invalid_err)


class TestConfigParsing(unittest.TestCase):
    """Testing related to parsing the config file for rsync_snap"""
    test_file_path = './tests/test.conf'

    def test_bad_key_order(self):
        """Should fail when profile key occurs after fields"""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

        # Create a profile where the profile name occurs after the settings
        config_bad_key_order = [
            'src: /tmp',
            'dst: /var/lib',
            '[invalid_profile]',
            '',
            '[valid_profile]',
            'src: /tmp',
            'dst: /var/lib',
            '',
            'src: /tmp',
            'dst: /var/lib',
            '[invalid_profile2]',
        ]

        # Create the map that is expected from this bad file
        expected_profile = {
            'valid_profile': {
                'src': '/tmp',
                'dst': '/var/lib',
            }
        }

        # Write the bad config to file
        with open(self.test_file_path, 'w') as f:
            for line in config_bad_key_order:
                f.write('{}\n'.format(line))




    pass



    # TODO: have the test create a test file, then pass it to func
    def test_parse_config_bad_profile_key(self):
        """Test if any key besides 'profile' in a config returns an empty
        dictionary"""
        profile_dict = {
            'correctProfile': {
                'src': '/tmp',
                'dst': '/var/lib'
            }
        }
        config_file = './tests/invalid-profiles.conf'
        self.assertEqual(parse_config(config_file), profile_dict)
