# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import os
from setuptools import setup, find_packages  # noqa: H301

NAME = "asana"
VERSION = "3.0.12"
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Asana",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Asana, Inc',
    url="http://github.com/asana/python-asana",
    keywords=["asana", "Asana"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
)
