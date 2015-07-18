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

Install
=======

Please refer to `vcs-pre-commit-buildout
<https://github.com/petrus-v/vcs-pre-commit-buildout>`_ `README.md` file
to install and configure it.

Roadmap
=======

* Flake8 hook
* jshint hook
* jslint hook