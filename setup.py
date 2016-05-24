#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thsr_moment_order
from setuptools import setup, find_packages

long_description = open('./README.md', 'r').read()
description = '嵌入式資料庫練習'

setup(name='embedded_nosql_databases',
      version='1.0.0',
      description=description,
      long_description=long_description,
      author='YUCHEN LIU',
      author_email='steny138@gmail.com',
      url='https://github.com/steny138/ThsrMomentOrder',
      packages=['embedded_nosql_databases'],
      package_data={'embedded_nosql_databases': ['*.csv']},
      include_package_data=True,
      license='LICENSE',
      keywords="unqlite sqlite leveldb bekerlydb " +
               "嵌入式資料庫 ",
      install_requires=['python-dateutil==1.5', 'ujson', 'urllib3'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Chinese (Traditional)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business :: Financial :: Investment',
      ],
      )
