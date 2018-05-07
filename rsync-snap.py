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

if __name__ == "__main__":
    # handle args
    import argparse

    DESC = "A profile-based incremental snapshot backup script"
    DESC += " that makes use of rsync's hard link functionality"
    DESC += " to make snapshots of changes in the backup directory "
    DESC += "with very little extra disk space."

    aparser = argparse.ArgumentParser(description=DESC)

    aparser.add_argument('backup-profile', metavar='BACKUP_PROFILE',
                         help='profile associated to backup configs in rsync-snap.yml')

    args = aparser.parse_args()
    print(args)
