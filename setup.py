from distutils.core import setup
from setuptools import find_packages

setup(
    name="vcs-pre-commit",
    version=0.1,
    author="Anybox",
    author_email="pverkest@anybox.fr",
    description="Useful vcs pre commit hooks",
    license="AGPL-3.0",
    long_description='\n'.join((
        open('README.rst').read(),
        open('CHANGES.rst').read())),
    platforms='linux',
    url="https://github.com/petrus-v/vcs-pre-commit",
    packages=find_packages('.', exclude=('tests*')),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
    tests_require=[],
    classifiers=[
        'License :: OSI Approved :: AGPL-3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'vcs-pre-commit = vcs_pre_commit.main:main',
        ],
    },
)
