# -*- coding: utf-8 -*-

from setuptools import setup

REPOSITORY = 'https://github.com/vulcan25/plugable-api'

__version__ = 0.1

setup(
    name='plugable-api',
    version=__version__,
    description='Plugable API compatibility for flask.',
    author='vulcan25',
    #author_email='',
    url=REPOSITORY,
    download_url='{}/tarball/{}'.format(REPOSITORY, __version__),
    modules=['plugable_api'],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    license='MIT',
    keywords=['Flask','plugable-api']
)