"""
Ridiculously lazy logger. Just a wrapper for Python's `logging` with color support.
```
    >>> log = lil_logger.get("logger name", lil_logger.DEBUG)
    >>> log.info("this is useful information")
```
"""

import logging
from colorama import Fore, Back

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

class LilFormatter(logging.Formatter):
    LOG_FORMAT = "[%(asctime)s][%(levelname)s] %(message)s"
    FORMATS = {
        logging.DEBUG: Fore.WHITE + LOG_FORMAT + Fore.RESET,
        logging.INFO: Fore.LIGHTBLUE_EX + LOG_FORMAT + Fore.RESET,
        logging.WARNING: Fore.YELLOW + LOG_FORMAT + Fore.RESET,
        logging.ERROR: Fore.RED + LOG_FORMAT + Fore.RESET,
        logging.CRITICAL: Back.RED+ Fore.WHITE + LOG_FORMAT + Fore.RESET + Back.RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        return logging.Formatter(log_fmt).format(record)

def get(name: str, level: int, log_format:str = None) -> logging.Logger:
    """
    Creates a :class:`logging.Logger` with the specified configurations,
    using colors for different message types.

    Args:
        name (str): Name of the logger.
        level (int): Level of info to output.
        log_format (str): Optional message formatting. Defaults to "[YYYY-MM-DD HH:mm:ss,sss][LEVEL] message".

    Returns
        logging.Logger: logger instance with formatting already set.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(LilFormatter())
    logger.addHandler(handler)

    return logger
