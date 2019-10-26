#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='emojis',
    version='0.5.0',
    author='Alexandre Vicenzi',
    author_email='pypi@alxd.me',
    maintainer='Alexandre Vicenzi',
    maintainer_email='pypi@alxd.me',
    packages=find_packages(exclude=("tests",)),
    url='https://github.com/alexandrevicenzi/emojis',
    bugtrack_url='https://github.com/alexandrevicenzi/emojis/issues',
    license='MIT',
    description='Emojis for Python',
    long_description=long_description,
    keywords='python, emoji, emojis, unicode',
    platforms='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Utilities',
    ],
)
