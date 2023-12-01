# logs/exceptions.py
import logging
import os
from .logging_ import Logger_

# ===============xERRORS
class ErrorHandler_(Exception):
    log_dir = '/logs/'
    log_file = os.path.join(log_dir, 'errors.log') 
    logger = Logger_(log_file='{log_dir}'+'errors.log')  # Create a class-level Logger_ instance assuming Logger_ class has an 'error' method
    def __init__(self, message, level=logging.ERROR):
        self.message = message
        self.level = level
        # Call the parent class (Exception) constructor with the message
        super().__init__(self.message)
    def handle_error(self):
        # Use the Logger_ instance to log the error
        ErrorHandler_.logger.error(self.message, self.level)
        print(self)
    """ #usage:
    try:
        # Some code that might raise an error
    except Exception as e:
        error_handler = ErrorHandler_('An error occurred: ' + str(e))
        error_handler.handle_error()  # This will log the error message
    """
# inherit from ErrorHandler_
class FallbackError(ErrorHandler_):
    def __init__(self):
        super().__init__("An unspecified error has occurred.")

    def handle_error(self):
        logging.error("FallbackError: " + self.message)

class BadRequestError(ErrorHandler_):
    def __init__(self):
        super().__init__("Bad Request: Malformed request")

    def handle_error(self):
        logging.error("BadRequestError: " + self.message)

class UnsupportedActionError(ErrorHandler_):
    def __init__(self):
        super().__init__("Unsupported Action: Unimplemented action")

    def handle_error(self):
        logging.error("UnsupportedActionError: " + self.message)

class BadParamError(ErrorHandler_):
    def __init__(self):
        super().__init__("Bad Param: Invalid parameter")

    def handle_error(self):
        logging.error("BadParamError: " + self.message)

class BadHandlerError(ErrorHandler_):
    def __init__(self):
        super().__init__("Bad Handler: Implementation error")

    def handle_error(self):
        logging.error("BadHandlerError: " + self.message)

class InternalHandlerError(ErrorHandler_):
    def __init__(self):
        super().__init__("Internal Handler Error: Uncaught exception")

    def handle_error(self):
        logging.error("InternalHandlerError: " + self.message)

class MethodNotImplementedError(ErrorHandler_):
    def __init__(self):
        super().__init__("Method Not Implemented: Method is absent")

class RateLimitExceededError(ErrorHandler_):
    def __init__(self):
        super().__init__("Rate Limit Exceeded: Too many requests")