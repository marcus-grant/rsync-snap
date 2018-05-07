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

def print_usage():
    """Helper function that prints out the usage for the for this utility...
    when the module is being used as a main script"""
    # TODO: Add more options like:
                # explicit options without configs:
                    # source dir
                    # dest dir
                    # logs dir
                    # remote identity file path
                    # remote identity HostName
                    # remote address
                    # remote user
                    # remote port
    # TODO: Create proflie creation prompt to guide users.
    print("rsync-snap usage:")
    print("========================================" + 
           "========================================")
    print("rsync-snap BACKUP_PROFILE_NAME")
    

if __name__ = "__main__":
    # handle args
