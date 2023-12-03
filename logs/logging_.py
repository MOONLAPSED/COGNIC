# logs/logging.py
# =================xIMPORTS
import datetime
import json
import logging
import os
import sys
import unittest
import logging
import requests

# ===============xLOGGING
import logging

class Logger_:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('ModuleName')
        self.logger.setLevel(logging.DEBUG)
        
        # Example to add a file handler to log messages to a file
        fh = logging.FileHandler('error.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def error(self, message, level):
        with open(self.log_file, 'a') as f:
            f.write(f'{message} [{level}]') 
        if level == logging.ERROR:
            self.logger.error(message)
