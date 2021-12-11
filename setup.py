#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name                = 'ml',
    version             = '0.1',
    description         = 'ml',
    packages            = find_packages(exclude = ['contrib', 'docs', 'tests*']),
    py_modules          = ['ml'],
    install_requires    = [
        'xmltodict',
        'aiohttp',
        'rsa',
        'hexdump',
    ],
)
