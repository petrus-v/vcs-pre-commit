import logging

from abc import ABCMeta, abstractmethod

from .util import check_call

logger = logging.getLogger(__name__)


class Hook(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def extensions(self):
        """extensions file allow by the hook
        :return: (list) extension file list manage by the hook
            (ie: ['.js', '.py'])
        """

    @abstractmethod
    def run(self, file):
        """Abstract method called to check changed file
        :param file: (string) path to the file to check
        :return: (int) 0 if there is no problem, hook programs error return by
        check_call"""


    def run_hook(self, file):
        """ Method to call to check hook
        :param file: (string) path to the file to check
        :return: (int) 0 if there is no problem, hook programs error return by
        check_call
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