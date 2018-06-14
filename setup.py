# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os
import subprocess

setup(
    name='toyrobot',
    version='0.1.0',
    description='Toy Robot (console application)',
    url='',
    author='Jonathan Newnham',
    author_email='jonathan.newnham@iress.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'toyrobot = toyrobot.__main__:main'
        ]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)

