#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'argparse>=1.4.0'
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    'argparse'
    # TODO(zoldello): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='fencing',
    version='1.0.0',
    description="Create pools for fencing participants",
    long_description=readme + '\n\n' + history,
    author="Philip Adenekan",
    author_email='greenish_green@yahoo.com',
    url='http://zoldello.wordpress.com',
    packages=find_packages(include=['fencing', 'fencing.model', 'fencing.service']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='fencing, fence, sports, UCSC, demo, Philip, Adenekan, pools, demo, practice, python',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'License :: Other/Proprietary License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Topic :: Education'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    entry_points = {
        "console_scripts": ["fencing = fencing.fencing:main"]
    }
)

__author__ = "Philip Adenekan"
