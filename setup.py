from setuptools import setup, find_packages
from sys import version_info
from pysendpulse import (
    __author__,
    __author_email__,
    __version__
)

install_requires = ['python3-memcached', ]

if version_info.major == 2:
    install_requires = ['python-memcached', 'requests', 'simplejson']

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='pysendpulse',
    version=__version__,
    packages=find_packages(),
    description='A simple SendPulse REST client library and example for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__author_email__,
    url='https://github.com/sendpulse/sendpulse-rest-api-python',
    install_requires=install_requires
)
