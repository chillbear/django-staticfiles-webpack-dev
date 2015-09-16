# coding=utf-8
"""
"""
from distutils.core import setup

version = '0.1'

setup(
  name = 'django-staticfiles-webpack-dev',
  packages = ['webpack'],
  version = version,
  description = 'Support for loading webpack-dev-server served files in Django templates via the static files app.',
  author = 'Ryan Gonzalez, Rocco Schulz',
  author_email = 'ryan@ionizedmedia.com',
  url = 'https://github.com/ryngonzalez/django-staticfiles-webpack-dev',
  download_url = 'https://github.com/ryngonzalez/django-staticfiles-webpack-dev/webpack/tarball/{}'.format(version),
  keywords = ['django', 'webpack', 'assets', 'build', 'static', 'webpack-dev-server'],
  classifiers = [
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Framework :: Django',
    'Environment :: Web Environment',
    'License :: OSI Approved :: MIT License',
  ],
)
