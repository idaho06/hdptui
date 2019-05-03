#!/usr/bin/env python3.6

import logging
import subprocess


def krbauth(principal, keytab):
    cmd = ['/usr/bin/kinit', '-kt', keytab, principal]
    success = subprocess.run(cmd, stdout=subprocess.DEVNULL).returncode
    logging.debug("Kinit cmd: "+ " ".join(cmd) + "\nReturn code: " + str(success))
    return not bool(success)
