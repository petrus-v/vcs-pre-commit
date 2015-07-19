import logging

from abc import ABCMeta, abstractmethod

from .util import call, which

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
    def run(self, check_file):
        """Abstract method called to check changed file
        :param file: (string) path to the file to check
        :return: (int) 0 if there is no problem, hook programs error return by
        check_call"""

    def run_hook(self, check_file):
        """ Method to call to check hook
        :param file: (string) path to the file to check
        :return: (int) 0 if there is no problem, hook programs error return by
        check_call
        """
        for ext in self.extensions():
            if check_file.endswith(ext):
                return self.run(check_file)
        return 0


class Flake8(Hook):

    def extensions(self):
        return ['.py']

    def run(self, check_file):
        return call([which('flake8'), check_file])


class JsHint(Hook):

    def extensions(self):
        return ['.js']

    def run(self, check_file):
        return call([which('jshint'), check_file])


class EsLint(Hook):

    def extensions(self):
        return ['.js']

    def run(self, check_file):
        return call([which('eslint'), check_file])