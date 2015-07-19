import logging
from subprocess import check_output as cmd_output, check_call as cmd_call

logger = logging.getLogger(__name__)


def check_call(cmd):
    logger.debug('check call: %r', cmd)
    return cmd_call(cmd)

def check_output(cmd):
    logger.debug('check output: %r', cmd)
    return cmd_output(cmd)
