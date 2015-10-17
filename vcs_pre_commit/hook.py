import logging

from abc import ABCMeta, abstractmethod

from .util import call, which

logger = logging.getLogger(__name__)


class Hook(object):
    __metaclass__ = ABCMeta

    def init(self, config=None):
        self.config = config

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
        '--config'
        cmd = [which('flake8')]
        if self.config and self.config.config:
            cmd += [self.config.config]
        return call(cmd + [check_file])


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


class XmlLint(Hook):

    def extensions(self):
        return ['.xml']

    def run(self, check_file):
        return call([which('xmllint'), '--noout', check_file])


class OdooLint(Hook):

    def extensions(self):
        return ['.xml', '.rst', '.py', '.js']

    def run(self, check_file):
        # bin/pylint --load-plugins=pylint_odoo -d all -e odoolint file.py
        return call([which('pylint'), '--load-plugins', 'pylint_odoo', '-e',
                     'odoolint', check_file])
