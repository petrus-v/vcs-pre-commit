from abc import ABCMeta, abstractmethod
from subprocess import check_output


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
        import pdb; pdb.set_trace()
        files = check_output(['git', 'status', '--porcelain', '-z']
                             ).decode("utf-8")
        return files.split('\x00')


class Hg(VCS):

    def commiting_files(self):
        files = check_output(['hg', 'status', '-m', '-a', '-n', '-0']
                             ).decode("utf-8")
        import pdb; pdb.set_trace()
        return files.split('\x00')