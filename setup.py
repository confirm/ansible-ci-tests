#!/usr/bin/env python
from distutils.core import setup

setup(
    name='ansibleci',
    packages=[
        'ansibleci',
        'ansibleci.tests',
    ],
    version='0.2.0',
    description='Ansbile CI tests',
    author='confirm IT solutions',
    author_email='pypi@confirm.ch',
    url='https://github.com/confirm/ansibleci',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
)
