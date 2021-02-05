#!/usr/bin/env python3
from setuptools import setup, find_packages
setup(
    name="tap-greenhouse",
    version="0.1.2",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    packages=find_packages(),
    install_requires=[
        "singer-python==5.2.0",
        'requests==2.18.4',
        "pendulum==1.2.0",
        "tap-kit @ git+https://github.com/Radico/tap-kit.git@bc4b936975f679a5887891036570daf1bab01c64"
    ],
    dependency_links=[
        "https://github.com/Radico/tap-kit/tarball/bc4b936975f679a5887891036570daf1bab01c64",
    ],
    entry_points="""
    [console_scripts]
    tap-greenhouse=tap_greenhouse:main
    """,
    include_package_data=True,
)
