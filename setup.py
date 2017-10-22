#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(zoldello): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='fencing',
    version='0.1.0',
    description="Create pools for fencing participants",
    long_description=readme + '\n\n' + history,
    author="Philip Adenekan",
    author_email='greenish_green@yahoo.com',
    url='http://zoldello.wordpress.com',
    packages=find_packages(include=['fencing']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='fencing, fence, sports, UCSC, demo, Philip, Adenekan',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    entry_points = {
        "console_scripts": ["fencing = fencing.fencing:main"]
    }
)
