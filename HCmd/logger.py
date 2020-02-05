# -*- coding: utf-8 -*-
from logging.handlers import TimedRotatingFileHandler
import logging
import os
import sys
from datetime import datetime

FORMATTER_FILE = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
FORMATTER_CONSOLE = FORMATTER_FILE
LOG_FILE = os.path.join("/home/jhewers/catkin_ws/src/asdp4_hornet","HCmd.log")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER_CONSOLE)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight', backupCount=10)
    file_handler.setFormatter(FORMATTER_FILE)
    return file_handler


class cust_logger(logging.Logger):
    def __init__(self, name, level = logging.NOTSET):
    	return super(cust_logger, self).__init__(name, level)      

    def error(self, msg, *args, **kwargs):
        return super(cust_logger, self).warning(msg, *args, **kwargs)

def get_logger(logger_name):
    logging.setLoggerClass(cust_logger)
    logging.basicConfig()

    logger = logging.getLogger(logger_name)
    
    # better to have too much log than not enough
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger


