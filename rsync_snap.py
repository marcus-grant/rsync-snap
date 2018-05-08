#!/usr/bin/env python3
"""Rsync-Snap
    A backup script meant to use the --link-dest feature and some
    directory management logic to create Time Machine - like backups.
"""
__author__ = "Marcus Grant"
__copyright__ = "None"
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Marcus Grant"
__email__ = "marcusfg@gmail.com"
__status__ = "Alpha"

import argparse
import os

# Easily accessible constants that contain different strings related to the CLI
PROG_NAME = "rsync_snap.py"
PROG_DESC = "A rsync based backup utility that adds to rsync " \
    "profiles & incremental snaphosts through hardlinks."
BACKUP_PROFILE_HELP = "backup profile to use for backup snapshot"
BACKUP_PROFILE_META = "BACKUP_PROFILE"

# Script default constants
CONFIG_FILENAME = "rsync_snap.yml"
CONFIG_PATH = os.getcwd()


# handle args
def get_args():
    """Setup & return an args namespace to later parse arguments"""
    aparser = argparse.ArgumentParser(prog=PROG_NAME,
                                      description=PROG_DESC)

    aparser.add_argument('backup_profile',
                         metavar='BACKUP_PROFILE',
                         help=BACKUP_PROFILE_HELP)
    return aparser.parse_args()

def validate_profile_name():
    legal_chars = '^[]'



if __name__ == "__main__":
    ARGS = get_args()
    PROFILE_NAME = ARGS.backup_profile
    print(PROFILE_NAME)
