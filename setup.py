"""
Py2ChainMap
==================

A backport of ChainMap from Python 3 to Python .
Get source from https://github.com/justanr/Py2ChainMap
"""
from setuptools import setup

setup(
    name='Py2ChainMap',
    version='0.1.0',
    author='kkxue',
    author_email='xueguanwen@gmail.com',
    description='A backport of ChainMap from Python 3 to Python 2.',
    long_description=__doc__,
    url='https://github.com/kkxue/Py2ChainMap/',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        ],
    platforms='any',
    py_modules=['py2chainmap', 'test_py2chainmap'],
    test_suite='test_py2chainmap.suite',
    )
