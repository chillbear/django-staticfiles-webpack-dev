# coding=utf-8
"""
"""
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import os
import json


class WebpackDevServerStorage(StaticFilesStorage):
    """
    Simple StaticFilesStorage based class that can be used together with the assets-webpack-plugin to include
    hashed files.
    
    Meant to be used alongside schocco/django-staticfiles-webpack in production, and this in development.

    The WEBPACK_ASSETS_FILE setting must be set and point to a valid json file.
    In the templates, entry point assets can then be referenced with their webpack name plus the appropriate suffix -
    e.g. with {% static 'entry1.js' %}
    """

    def __init__(self, assets_file=None, *args, **kwargs):
        # check if assets file present
        if assets_file is None:
            self.assets_file = settings.WEBPACK_ASSETS_FILE
        self.check_assets()
        self.load_json()
        super(WebpackDevServerStorage, self).__init__(*args, **kwargs)

    def check_assets(self):
        """
        Throws an exception if assets file is not configured or cannot be found.
        :param assets: path to the assets file
        """
        if not self.assets_file:
            raise ImproperlyConfigured("You must specify the path to the assets.json file via WEBPACK_ASSETS_FILE")
        elif not os.path.exists(self.assets_file):
            raise ImproperlyConfigured(
                "The file `{file}` was not found, make sure to run the webpack build before the collectstatic command".format(
                    file=self.assets_file))

    def load_json(self):
        with open(self.assets_file) as json_file:
            self.assets = json.load(json_file)

    def url(self, name):
        """

        :param name: either the name of the webpack entry point (plus suffix like .js or .sourcemap) or the name of
            any other static file
        :return: path using the filename found in the assets.json file generated by webpack, if the name is not
            present in the json file, then the call is delegated to the super class.
        """
        split = os.path.splitext(name)
        raw_name = split[0]
        suffix = split[1].lstrip('.') if len(split) > 1 else "js"
        print(self.assets)
        print(raw_name)
        print(suffix)
        if self.assets.has_key(raw_name) and self.assets.get(raw_name).has_key(suffix):
            name = self.assets.get(raw_name).get(suffix)
            print(name)
            return name
        return super(WebpackDevServerStorage, self).url(name)
