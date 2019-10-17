# coding: utf-8
import os
from setuptools import setup, find_packages

long_description = open('README.rst' if os.path.exists('README.rst') else 'README.md').read()

setup(
    name='pdalinfo2rst',
    version='0.0.1',
    packages=find_packages(),
    license='MIT',
    description='Convert "pdal info" JSON to "ReStructured text"',
    url='https://github.com/hobu/pdalinfo2rst',
    author='Howard Butler',
    install_requires=open('requirements.txt').read(),
    include_package_data=True,
    test_suite='pdal2rst.test',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Documentation',
    ],
    entry_points={
        'console_scripts': [
            'pdal2rst = pdal2rst.pdalinfo2rst:main',
        ]
    }
)
