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
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union
from abc import ABCMeta, abstractmethod
# ===============xLOGGING
import logging


T = TypeVar("T")
"""
Define a generic `Logger_` class that can be used to log messages to standard output or to a file. We have also defined a `Config` object that can be used to configure the logger. The `App` object uses the `Config` object to get a logger and then uses the logger to log messages.
"""
class Logger_(metaclass=ABCMeta):
    """A generic logger class."""

    @abstractmethod
    def log(self, message: str, level: str) -> None:
        """Log a message at the specified level."""

class StdoutLogger(Logger_):
    """A logger that writes messages to standard output."""

    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def log(self, message: str, level: str) -> None:
        self._logger.log(level, message)

    def get_logger(self, name: str) -> Logger_:
        return StdoutLogger()

class FileLogger(Logger_):
    """A logger that writes messages to a file."""

    def __init__(self, filename: str):
        self._logger = logging.getLogger(__name__)
        self._fh = logging.FileHandler(filename)
        self._formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        self._logger.addHandler(self._fh)

    def log(self, message: str, level: str) -> None:
        self._logger.log(level, message)

    def get_logger(self, name: str) -> Logger_:
        return FileLogger(filename)

    @abstractmethod
    def get_logger(self, name: str) -> Logger_:
        """Get a logger for the specified name."""

class Config:
    """A configuration object."""

    def __init__(self):
        self._logger_type: Type[Logger_] = StdoutLogger
        self._logger_type = logger_type

    def set_logger_name(self, logger_name: str) -> None:
        """Set the logger name."""
        self._logger_name = logger_name

    def get_logger(self) -> Logger_:
        """Get a logger."""
        return self._logger_type(self._logger_name)

class App:
    """An application object."""

    def __init__(self, config: Config) -> None:
        self._config = config
        self._logger = self._config.get_logger()

    def run(self) -> None:
        """Run the application."""
        self._logger.log("Starting application...")
        # test, app logic, etc
        self._logger.log("Stopping application...")

if __name__ == "__main__":
    config = Config()
    config.set_logger_type(StdoutLogger)
    config.set_logger_name("default")
    app = App(config)
    app.run()