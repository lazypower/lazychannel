from distutils.core import setup
from setuptools import find_packages

setup(
    name="lazychannel",
    version="0.1.1",
    description="Fetch things daily!",
    license="LGPLv3",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'lazy = lazychannel.cli:main'
        ],
    },
    install_requires=[
        'requests',
        'pyyaml',
        'youtube-dl',
    ],
)
