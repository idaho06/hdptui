#!/usr/bin/env python3.6

# -*- coding: utf-8 -*-

# Imports
import logging
import argparse
import util.config


# Globals and other helper functions


def main(args):
    logging.debug("Entering Main function")
    print("Hello, world!.")
    print("These are your args:")
    print(args)
    print(config._CONFIG_FILE)

    # profit!
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HDP Text User Interface.",
                                     epilog="Made by César (Idaho06) Rodríguez Moreno.")
    # parser.add_argument("echo", help="echo the string you use here")
    # parser.add_argument("-db", "--database", help="Database to be used.", default="/tmp/termgame.sqlite3")
    parser.add_argument("-d", "--debug", help="Debug level: DEBUG, INFO, WARNING, ERROR or CRITICAL", default="WARNING")
    parser.add_argument("-o", "--erroroutput", help="File of error output. Default is stderr.", default="stderr")
    parser.add_argument("-c", "--config", help="Sets configuration file. Default is hdptui.ini", default="hdptui.ini")
    args = parser.parse_args()

    loglevel = logging.WARNING
    logoutput = None
    if args.debug == "DEBUG":
        loglevel = logging.DEBUG
    if args.debug == "INFO":
        loglevel = logging.INFO
    if args.debug == "ERROR":
        loglevel = logging.ERROR
    if args.debug == "CRITICAL":
        loglevel = logging.CRITICAL
    if args.erroroutput != "stderr":
        logoutput = args.erroroutput
    logging.basicConfig(level=loglevel, filename=logoutput,
                        format="%(asctime)s %(levelname)s: %(funcName)s: %(message)s")
    logging.info("Logging level set to %s." % logging.getLevelName(loglevel))
    # logging.info("Configuring database to %s" % args.database)

    config = util.config.ConfigClass(args.config)

    exit(main(args))
