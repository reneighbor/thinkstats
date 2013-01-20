#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="thinkstats",
    version="0.0.1",
    description="General-purpose functions used throughout thinkstats.",
    author="Allen B. Downey",
    tests_require=[
        'nose'
    ]
)