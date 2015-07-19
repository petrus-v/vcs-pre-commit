import logging
from argparse import ArgumentParser
from .vcs import VCS

logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser(description="VCS PRE COMMIT")
    parser.add_argument('--logging-level', default='INFO')
    parser.add_argument('--vcs', default='git', choices=['git', 'hg'],
                        help="vcs currently in use")
    arguments = parser.parse_args()

    logging.basicConfig(level=getattr(logging,
                                      arguments.logging_level.upper()))
    logger.info("%(vcs)s pre-commit hook", dict(vcs=arguments.vcs, ))
    repo = VCS.get_instance(arguments.vcs)
    logger.info("%r", repo.commiting_files())
    status = 0
    return status
