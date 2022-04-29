import logging
from logging import config
from typing import *

from log_config import LOG_CONFIG


class Logger:

    @staticmethod
    def get(name: Optional[str]=None) -> logging.Logger:
        config.dictConfig(LOG_CONFIG)
        logger = logging.getLogger('FileLogger')
        return logger
