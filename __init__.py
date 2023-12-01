# /__init__.py
import sys
import os
# Start with the current directory
SafeDir_ = os.getcwd()
# Keep going up one directory at a time until 'COGNIC' is found or the root is reached
while not os.path.basename(SafeDir_) == 'COGNIC':
    parent_dir = os.path.dirname(SafeDir_)
    if parent_dir == SafeDir_:  # We've reached the root, 'COGNIC' was not found
        raise Exception('COGNIC not found')
    SafeDir_ = parent_dir
# At this point, SafeDir_ is the 'COGNIC' directory
# Add it to the Python path if it's not already there
if SafeDir_ not in sys.path:
    sys.path.append(SafeDir_)
# =================xLOGGING
from logs.exceptions_ import *
from logs.logging_ import *

log_dir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


__all__ = ['e_', 'l_', 'SafeDir_']
