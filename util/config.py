#!/usr/bin/env python3.6

import configparser
import logging


class ConfigClass:
    """ Class for controlling configurations"""
    _CONFIG_FILE = 'test/testconfig.ini'
    parser = None

    def __init__(self, configfile=None):
        logging.debug("Received configuration file is: " + str(configfile))
        if configfile is not None:
            self._CONFIG_FILE = configfile

        self.parser = configparser.ConfigParser()
        try:
            self.parser.read(self._CONFIG_FILE)
        except:
            logging.critical("Unexpected error:", sys.exc_info()[0])
            raise
