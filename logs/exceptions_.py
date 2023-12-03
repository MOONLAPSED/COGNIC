# logs/exceptions.py
import logging
import os
from .logging_ import Logger_

# ===============xERRORS
class ErrorHandler_(Exception):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    logger = Logger_(log_file=log_file)  # Create a class-level Logger_ instance assuming Logger_ class has an 'error' method
    def __init__(self, message, level=logging.ERROR):
        self.message = message
        self.level = level
        # Call the parent class (Exception) constructor with the message
        super().__init__(self.message)
    def handle_error(self):
        print(self)
    """ #usage:
    try:
        # Some code that might raise an error
    except Exception as e:
        error_handler = ErrorHandler_('An error occurred: ' + str(e))
        error_handler.handle_error()  # This will log the error message
    """
    def __str__(self):
        return self.message
    # Exception base class (Exception) constructor
    while True:
        try:
            raise Exception("An error occurred.")
            break
        except Exception as e:
            logger.error(e, level=logging.ERROR)
            break
# inherit from ErrorHandler_
class FallbackError(ErrorHandler_):
    def __init__(self):
        super().__init__("An unspecified error has occurred.")
        super().handle_error()

    def handle_error(self):
        logging.error("FallbackError: " + self.message)

    def __str__(self):
        return "FallbackError: " + self.message
