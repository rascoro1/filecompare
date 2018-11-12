
from setuptools import setup

setup(
    name = 'filecompare',
    version = '0.1.0',
    packages = ['filecompare'],
    entry_points = {
        'console_scripts': [
            'filecompare = filecompare.__main__:main'
        ]
    })