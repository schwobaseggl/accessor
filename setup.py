# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='accessor',
    version='0.1',
    description='A simple python module for resolving paths on python objects',
    long_description=open('README.rst').read(),
    author='Veit Rückert',
    author_email='veit.rueckert@web.de',
    maintainer='Veit Rückert',
    maintainer_email='veit.rueckert@web.de',
    url='http://github.com/schwobaseggl/accessor',
    packages=find_packages(where=('accessor',)),
    keywords="accessor attribute key index resolve",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License (GPL)"
    ],
    install_requires=[],
)
