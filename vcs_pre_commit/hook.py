import logging

from abc import ABCMeta, abstractmethod

from .util import check_call

logger = logging.getLogger(__name__)


class Hook(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def extensions(self):
        """list of extension expected by the
        :return: (list) List of extension manage by hook
        """

    @abstractmethod
    def run(self, file):
        """
        :param file:
        :return:
        """

    def run_hook(self, file):
        """
        :param file:
        :return:
        """
        for ext in self.extensions():
            if file.endswith(ext):
                return self.run(file)


class Flake8(Hook):

    def extensions(self):
        return ['.py']

    def run(self, file):
        return check_call(['flake8', file])


class JsHint(Hook):

    def extensions(self):
        return ['.js']

    def run(self, file):
        return check_call(['jshint', file])