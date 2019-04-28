#!/usr/bin/python

from distutils.core import setup

setup(name='ooflang',
      version='0.1',
      description='Replaces the tokens in your C/C++ project with oofs that decrease readability',
      author='Dan Habot',
      author_email='dan.habot@gmail.com',
      url='https://github.com/danhab99/ooflang',
      packages=['ooflang'],
      scripts=['./ooflang.py'],
      entry_points={
          'console_scripts': ['ooflang=ooflang:main'],
      }
      )
