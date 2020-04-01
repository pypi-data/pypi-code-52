from setuptools import setup
import streamsx.sttgateway
setup(
  name = 'streamsx.sttgateway',
  packages = ['streamsx.sttgateway'],
  include_package_data=True,
  version = streamsx.sttgateway.__version__,
  description = 'Speech To Text gateway integration for IBM Streams',
  long_description = open('DESC.txt').read(),
  author = 'IBM Streams @ github.com',
  author_email = 'hegermar@de.ibm.com',
  license='Apache License - Version 2.0',
  url = 'https://github.com/IBMStreams/pypi.streamsx.sttgateway',
  keywords = ['streams', 'ibmstreams', 'streaming', 'analytics', 'streaming-analytics', 'sttgateway'],
  classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  install_requires=['streamsx>=1.14.6,<2.0'],
  
  test_suite='nose.collector',
  tests_require=['nose']
)
