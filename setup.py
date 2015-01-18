from distutils.core import setup
from setuptools import find_packages

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Environment :: Console',
    'Topic :: Multimedia :: Sound/Audio',
]

setup(
    name="lazychannel",
    version="0.1.4",
    description="Fetch media from remote sources daily!",
    author="Charles Butler",
    author_email="chuck@dasroot.net",
    url="https://github.com/chuckbutler/lazychannel",
    download_url="https://github.com/chuckbutler/lazychannel/tarball/v0.1.3",
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
