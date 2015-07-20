import logging
import os

from argparse import ArgumentParser

from .vcs import VCS
from .hook import Flake8, JsHint, EsLint, XmlLint

logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser(description="VCS PRE COMMIT")
    parser.add_argument('--logging-level', default='INFO')
    parser.add_argument('--vcs', default='git', choices=['git', 'hg'],
                        help="vcs currently in use")
    arguments = parser.parse_args()

    logging.basicConfig(level=getattr(logging,
                                      arguments.logging_level.upper()))
    logger.debug("%(vcs)s pre-commit hook", dict(vcs=arguments.vcs, ))
    repo = VCS.get_instance(arguments.vcs)
    files = repo.commiting_files()
    logger.debug("Audited files %r", files)
    hooks = [Flake8(), JsHint(), EsLint(), XmlLint()]
    first_error_number = None
    error_file = []
    for fpath in files:
        if not fpath:
            continue
        if not os.path.isfile(fpath):
            first_error_number = 1
            logger.error("Weird, file: %s not found, can't be tested", fpath)
            continue
        logger.debug("-   ===== Start checking %r =====   -", fpath)
        for hook in hooks:
            hook_result = hook.run_hook(fpath)
            if hook_result != 0:
                if not first_error_number:
                    first_error_number = hook_result
                error_file.append(fpath)
    if first_error_number:
        error_file = set(error_file)
        logger.warn("%(number)s files with errors %(files)r",
                    dict(number=len(error_file), files=error_file))
    logger.debug("End of vcs-pre-commit")
    return first_error_number
