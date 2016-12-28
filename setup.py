# coding:utf-8

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

VERSION = '0.1.0'

setup(name='nose-sigterm',
      version=VERSION,
      description='Raise KeyboardInterrupt on SIGTERM',
      url='https://github.com/scoutexchange/nose-sigterm',
      classifiers=['Intended Audience :: Developers',
                   'Topic :: Software Development :: Testing',
                   'Programming Language :: Python'],
      py_modules=['nose_sigterm'],
      zip_safe=False,
      entry_points={
        'nose.plugins': ['nose_sigterm = nose_sigterm:NoseSigterm']
      },
      install_requires=['nose'])
