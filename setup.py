# setup.py

from setuptools import setup, find_packages

setup(
    name='pyalgolab',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'networkx',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'pyalgolab=cli:main'
        ]
    }
)
