"""
Ridiculously lazy logger. Just a wrapper to Python's `logging`
with color support.
"""

import logging
from colorama import Fore, Back

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
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(LilFormatter())
    logger.addHandler(handler)

    return logger
