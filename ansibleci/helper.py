# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
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

    def get_roles_paths(self):
        '''
        Returns all absolute paths to the roles/ directories, while considering
        the ``BASEDIR`` and ``ROLES`` config variables.
        '''
        roles  = []

        for path in self.config.ROLES:
            roles.append(self.get_absolute_path(path))

        return roles

    def get_playbooks_path(self):
        '''
        Returns the absolute path to the playbooks/ directory, while considering
        the BASEDIR and PLAYBOOKS config variables.
        '''
        return os.path.abspath(os.path.join(self.config.BASEDIR, self.config.PLAYBOOKS))

    def get_playbooks(self):
        '''
        Returns a key-value dict with playbooks, while the key is the playbook name
        and the value is the absolute playbook path.
        '''
        plays = {}
        path  = self.get_playbooks_path()

        for entry in os.listdir(path):
            playpath = os.path.join(path, entry)
            if os.path.isfile(playpath):
                plays[entry] = playpath

        return plays

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
            return yaml.load(f)

    def get_yaml_items(self, dir_path, param=None):
        '''
        Loops through the dir_path and parses all YAML files inside the
        directory.

        If no param is defined, then all YAML items will be returned
        in a list. If a param is defined, then all items will be scanned for
        this param and a list of all those values will be returned.
        '''

        result = []

        if not os.path.isdir(dir_path):
            return []

        for filename in os.listdir(dir_path):

            path  = os.path.join(dir_path, filename)
            items = self.read_yaml(path)

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
        except AttributeError:
            return 'unknown'
