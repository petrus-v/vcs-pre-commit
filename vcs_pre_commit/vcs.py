from abc import ABCMeta, abstractmethod

from .util import check_output


class VCS(object):
    __metaclass__ = ABCMeta
    instance = None

    @classmethod
    def get_instance(cls, vcs_name):
        # if cls.instance is not None:
        #     return cls.instance
        if vcs_name == 'hg':
            return Hg()
        elif vcs_name == 'git':
            return Git()

    @abstractmethod
    def commiting_files(self):
        """Abstract method that return the list of changes files
        :return: list of path to changes files
        """


class Git(VCS):

    def commiting_files(self):
        status = check_output(['git', 'status', '--porcelain', '-z']
                             ).decode("utf-8")
        files = []
        for status in status.split('\x00'):
            if status.startswith('A') or status.startswith('M'):
                files.append(status.split(' ')[-1])
        return files



class Hg(VCS):

    def commiting_files(self):
        files = check_output(['hg', 'status', '-m', '-a', '-n', '-0']
                             ).decode("utf-8")
        return files.split('\x00')