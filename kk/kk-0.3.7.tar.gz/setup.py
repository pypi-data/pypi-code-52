#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: zhangkai
Last modified: 2020-04-01 18:01:35
'''

import os
from setuptools import setup, find_packages

data_files = []
os.chdir('kk')
for dirname in ['templates', 'static']:
    for root, _, files in os.walk(dirname):
        data_files.extend([os.path.join(root, fname) for fname in files])
os.chdir('..')

setup(
    name="kk",
    version='0.3.7',
    description="a simple file server",
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    author="zhangkai",
    author_email="zkdfbb@qq.com",
    url="http://www.ishield.cn",
    license="MIT",
    python_requires='>=3.5',
    install_requires=["markdown", "pyaml", "pymongo", "tornado", "kkutils>=1.1.3"],
    package_data={'': data_files},
    packages=find_packages(),
    entry_points={
        'console_scripts': ['kk=kk.index:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
    ]
)
