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
    author="Charles Butler",
    author_email="chuck@dasroot.net",
    url="https://github.com/chuckbutler/lazychannel",
    download_url="https://github.com/chuckbutler/lazychannel/archive/v0.1.2.tar.gz",
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
