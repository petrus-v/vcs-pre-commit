==============
VCS-PRE-COMMIT
==============

This is ``pre-commit`` hook to install to your favorite vcs. The purpose is to
set pre-commit hooks that will be use on every projects.

Current vcs supported are:
* mercurial
* git

Usage
=====

Depending vcs in used, commit your changes (``hg ci -m "commit message"``
or git commit -m "commit message"), ``vcs-pre-commit`` hook will be call.

Design
======

When you commit, only changes files will be give to your favorites programming
errors detectors. If there is an error commit process will be stopped.

Hooks
=====

flake8
------

config
~~~~~~

As mentionned in ``flake8 --help``, you can configure flake8 in
``~/.config/flake8`` file.

Install
=======

Please refer to `vcs-pre-commit-buildout
<https://github.com/petrus-v/vcs-pre-commit-buildout>`_ `README.md` file
to install and configure it.

Roadmap
=======

* implement vcs (with unit test!)
* implement hooks
    * Flake8 hook
    * jshint hook
    * jslint hook
    * xmlint
* hooks configuration (per project directory ?)
* configuration set to easly switch from one to another config
  * vcs-pre-commit --config-list
  * vcs-pre-commit --switch <config_name>
* extract hooks outside this code as pluggins
* run it outside hooks (on change files or all files)