import logging

from argparse import ArgumentParser

from .vcs import VCS
from .hook import Flake8, JsHint

logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser(description="VCS PRE COMMIT")
    parser.add_argument('--logging-level', default='DEBUG')
    parser.add_argument('--vcs', default='git', choices=['git', 'hg'],
                        help="vcs currently in use")
    arguments = parser.parse_args()

    logging.basicConfig(level=getattr(logging,
                                      arguments.logging_level.upper()))
    logger.debug("%(vcs)s pre-commit hook", dict(vcs=arguments.vcs, ))
    repo = VCS.get_instance(arguments.vcs)
    files = repo.commiting_files()
    logger.debug("Audited files %r", files)
    hooks = [Flake8(), JsHint()]
    first_error_number = 0
    for file in files:
        logger.info("Start checking %r", file)
        for hook in hooks:
            hook_result = hook.run_hook(file)
            if first_error_number == 0 and hook_result != 0:
                first_error_number = hook_result
    return first_error_number