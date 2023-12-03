# /__init__.py
# =================xGLOBAL_IMPORTS
import sys
import os
import json
import logging
import unittest
import datetime
import re
# =================xLOGGING
from logs.exceptions_ import *
from logs.logging_ import *

try:
    logger = Logger_()
    SafeDir_ = ['/cognic/', '/COGNIC/', '/cognic/*', '/COGNIC/*']
    __all__ = ['e_', 'l_', 'SafeDir_', 'log_dir_', 'logger', 'stat_', '']
    sys.path.append(SafeDir_)
    log_dir = os.path('/logs/')
    log_dir_ = os.path.join(os.path.dirname(__file__), log_dir)
    if not os.path.exists(log_dir_):
        os.makedirs(log_dir_)
        logger.info('Created log directory.')
    else:
        logger.info('Log directory already exists.')
except:
    raise Exception('COGNIC/cognic not found')
    sys.exit()

class UUtils_(object):
    def stat_(path):
        """
        Get the stat information for the given path.

        :param path: the path to the file or directory
        :return: a tuple containing the stat information (st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime)
        """  # Use the `os.scandir()` function to get the stat information
        for info in os.scandir(path):
            if info.is_dir():
                # If the path is a directory, return the stat information for the directory
                return info.stat()
            elif info.is_file():  # If the path is a file, return the stat information for the file
                return info.stat()  # If the path is not a directory or a file, raise an exception
        raise IOError(f"{path} is not a directory or a file")

    def get_file_size(path):
        """
        Get the size of the file or directory at the given path.
        """
        try:
            return stat_(path)[stat_.st_size]
        except:
            raise IOError(f"Could not get the size of {path}")
    def get_file_mtime(path):
        """
        Get the modification time of the file or directory at the given path.
        """
        try:
            return stat_(path)[stat_.st_mtime]
        except:
            raise IOError(f"Could not get the modification time of {path}")
    def find_files(path, pattern):
        """
        Find all files in the given path that match the given pattern.
        """
        try:
            for root, dirs, files in os.walk(path):
                for basename in files:
                    if re.search(pattern, basename):
                        filename = os.path.join(root, basename)
                        yield filename
            return True
        except:
            return False
            raise IOError(f"Could not find files in {path} matching {pattern}")
    def get_file_contents(path):
        """
        Get the contents of the file at the given path.
        """
        try:
            with open(path, 'r') as f:
                return f.read()
            return True
        except:
            return False
            raise IOError(f"Could not open {path} for reading")
    def get_file_contents_as_list(path):
        """
        Get the contents of the file at the given path.
        """
        try:
            with open(path, 'r') as f:
                return f.readlines()
            return True
        except:
            return False
            raise IOError(f"Could not open {path} for reading")
    def get_file_contents_as_json(path):
        """
        Get the contents of the file at the given path.
        """
        try:
            with open(path, 'r') as f:
                return json.load(f)
            return True
        except:
            return False
            raise IOError(f"Could not open {path} for reading")
    def write_file_contents(path, contents):
        """
        Write the given contents to the file at the given path.
        """
        try:
            with open(path, 'w') as f:
                f.write(contents)
            return True
        except:
            return False
            raise IOError(f"Could not open {path} for writing")
    def write_file_contents_as_json(path, contents):
        """
        Write the given contents to the file at the given path.
        """
        try:
            with open(path, 'w') as f:
                json.dump(contents, f)
            return True
        except:
            return False
            raise IOError(f"Could not open {path} for writing")
    def append_file_contents(path, contents):
        """
        Append the given contents to the file at the given path.
        """
        try:
            with open(path, 'a') as f:
                f.write(contents)
            return True
        except:
            return False
            raise IOError(f"Could not open {path} for appending")
    def append_file_contents_as_json(path, contents):
        """
        Append the given contents to the file at the given path.
        """
        try:
            with open(path, 'a') as f:
                json.dump(contents, f)
            return True
        except:
            return False
            raise IOError(f"Could not open {path} for appending")
    def create_file(path):
        """
        Create the file at the given path.
        """
        try:
            with open(path, 'x') as f:
                pass
            return True
        except:
            return False
    def create_dir(path):
        """
        Create the directory at the given path.
        """
        try:
            os.mkdir(path)
            return True
        except:
            return False