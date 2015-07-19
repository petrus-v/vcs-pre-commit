import logging
import os
import sys

from subprocess import call as cmd_call, check_output as cmd_output

logger = logging.getLogger(__name__)


def call(cmd):
    logger.debug('check call: %r', cmd)
    return cmd_call(cmd)


def check_output(cmd):
    logger.debug('check output: %r', cmd)
    return cmd_output(cmd)


def which(program):
    """Try to use buildout exec file before system one"""

    def is_exe(prog):
        return os.path.isfile(prog) and os.access(prog, os.X_OK)

    if is_exe(program):
        return program

    fpath, fname = os.path.split(program)
    for path in sys.path:
        if is_exe(os.path.join(path, fname)):
            return os.path.join(path, fname)

    exe = check_output(['which', fname]).decode('utf-8')
    if is_exe(exe):
        return exe
    return program
