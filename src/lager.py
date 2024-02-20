import logging
from logging.config import dictConfig
import sys
import threading
from logging.handlers import RotatingFileHandler 

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,   
    'formatters': {
        'default': {
            'format': '[%(levelname)s]%(asctime)s||%(name)s: %(message)s',
            'datefmt': '%Y-%m-%d~%H:%M:%S%z'
        },
    },
    'handlers': {
        'console': {
            'level': logging.INFO,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': logging.INFO,
            'formatter': 'default',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/app.log',
            'maxBytes': 10485760,
            'backupCount': 10
        }
    },
    'root': {  
        'level': logging.INFO,
        'propagate': True,
        'handlers': ['console', 'file']
    }
}
class Logger():
    _lock = threading.Lock()
    root_logger = None
    LOGGING_CONFIG = LOGGING_CONFIG
    
    @classmethod
    def get_logger(cls):
        with cls._lock:
            if cls.root_logger is None:
                logging.config.dictConfig(cls.LOGGING_CONFIG)
                cls.root_logger = logging.getLogger()
        return cls.root_logger

    @classmethod
    def branch_logger(cls, name):
        branch = '.'.join([cls.root_logger.name, name])
        return logging.getLogger(branch)

    @classmethod
    def get_logger_from_name(cls, name):
        return cls.get_logger().getChild(name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.root_logger}, level={self.root_logger.level})"

def run():  # this is the entry point for the module when imported or executed
    root()
    branch("branch")
    return root, branch

logger = None
branch_logger = None

def root():
    global logger  # Use the global logger variable
    logger = Logger.get_logger()  # Get the root logger
    try:
        logger.info(f"|{logger}|-has_handlers-|{logger.handlers}|")
    except NameError as e:
        print(f"Logging error: {e}")
    finally:
        # ...
        pass
    return logger

def branch(logger=None):
    branch_logger = Logger.get_logger_from_name("branch")  # Get a branch logger
    try:
        branch_logger.info(f"|{branch_logger}|-has_handlers-|{branch_logger.handlers}|")
    except NameError as e:
        print(f"Logging error: {e}")
    finally:
        # ...
        pass
    return branch_logger





if __name__ == "__main__":
    run()  # if setup.py is not invoked, and pip installs recursively the requirements.txt file, then this is the only entry point for the module

else:
    try:
        main.main()  # Call the main function from main.py
    except Exception as e:
        print(e)
    finally:
        # ...
        pass
