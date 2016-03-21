# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import re
import yaml


class Helper(object):
    '''
    Helper class which provides common used helper methods.
    '''

    def __init__(self, config):
        '''
        Class constructor which caches the config instance for later access.
        '''
        self.config = config

    def get_absolute_path(self, path):
        '''
        Returns the absolute path of the ``path`` argument.

        If ``path`` is already absolute, nothing changes. If the ``path`` is
        relative, then the BASEDIR will be prepended.
        '''
        if os.path.isabs(path):
            return path
        else:
            return os.path.abspath(os.path.join(self.config.BASEDIR, path))

    def get_file_extension(self, file):
        '''
        Returns the file extension of a file. The ``file`` argument can be
        a simple filename or a absoulte path.
        '''
        return '.'.join(os.path.basename(file).split('.')[1:])

    def get_roles_paths(self):
        '''
        Returns all absolute paths to the role directories, while considering
        the ``BASEDIR`` and ``ROLES`` config variables.
        '''
        roles  = []

        for path in self.config.ROLES:
            roles.append(self.get_absolute_path(path))

        return roles

    def get_playbook_paths(self):
        '''
        Returns all absolute paths to the playbook directories, while considering
        the ``BASEDIR`` and ``PLAYBOOKS`` config variables.
        '''
        playbooks  = []

        for path in self.config.PLAYBOOKS:
            playbooks.append(self.get_absolute_path(path))

        return playbooks

    def get_roles(self):
        '''
        Returns a key-value dict with a roles, while the key is the role name
        and the value is the absolute role path.
        '''
        roles = {}
        paths = self.get_roles_paths()

        for path in paths:
            for entry in os.listdir(path):
                rolepath = os.path.join(path, entry)
                if os.path.isdir(rolepath):
                    roles[entry] = rolepath

        return roles

    def read_yaml(self, filename):
        '''
        Reads and parses a YAML file and returns the content.
        '''
        with open(filename, 'r') as f:
            d = re.sub(r'\{\{ *([^ ]+) *\}\}', r'\1', f.read())
            y = yaml.safe_load(d)
            return y if y else {}

    def verify_yaml_file(self, file_path):
        '''
        Return True or False, if the ``file_path`` is a file and the
        file extension matchs the ``YAML_FILE_EXENTSIONS``.
        '''
        if os.path.isfile(file_path) and self.get_file_extension(file_path) in self.config.YAML_FILE_EXENTSIONS:
            return True
        else:
            return False

    def get_yaml_files(self, dir_path, recursive=False):
        '''
        Returns a list of all yaml files in a directory.
        '''
        result = []

        if not os.path.isdir(dir_path):
            return []

        if recursive:
            for root, dirname, filenames in os.walk(dir_path):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    if self.verify_yaml_file(file_path):
                        result.append(file_path)
            return result

        else:
            for filename in os.listdir(dir_path):
                file_path = os.path.join(dir_path, filename)
                if self.verify_yaml_file(file_path):
                    result.append(file_path)
            return result

    def get_yaml_items(self, dir_path, param=None):
        '''
        Loops through the dir_path and parses all YAML files inside the
        directory.

        If no param is defined, then all YAML items will be returned
        in a list. If a param is defined, then all items will be scanned for
        this param and a list of all those values will be returned.
        '''
        result = []

        for filename in self.get_yaml_files(dir_path):
                items = self.read_yaml(filename)

                for item in items:
                    if param:
                        if param in item:
                            item = item[param]
                            if isinstance(item, list):
                                result.extend(item)
                            else:
                                result.append(item)
                    else:
                        result.append(item)

        return result

    def get_item_identifier(self, item):
        '''
        Returns the identifier of a (task) item, which by default is the name
        param of the item. If no name param is defined then the method will
        return "unknown".

        @todo: Update this method to consider other params when name is not
        defined (e.g. "include").
        '''
        try:
            return item['name']
        except KeyError:
            return 'unknown'
