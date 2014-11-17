from distutils.core import setup
from setuptools import find_packages

CLASSIFIERS = [
    'Intended Audience :: Robots',
    'License :: OSI Approved :: LGPLV3 License',
    'Operating System :: OS Independent',
    'Topic :: Media Aggregation',
]

setup(
    name="lazychannel",
    version="0.1.2",
    description="Fetch media from remote sources daily!",
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
    classifiers=CLASSIFIERS,
)
