# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ansibleci.test import Test
import os


class Prefix(Test):
    '''
    Test to check if all role variables are prefixed with the rolename.

    The default prefix of a role is <rolename> with a seperator, which
    can be configured in the settings ``PREFIX_SEPERATOR``.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        self.config = self.get_config()
        self.helper = self.get_helper()

        for role, path in self.helper.get_roles().iteritems():
            for subdir in self.config.PREFIX_VARIABLE_DIRECTORIES:
                self.check_prefix(role, os.path.join(path, subdir))

    def check_prefix(self, role, directory):
        '''
        Check the role variables for a defined prefix.
        '''
        items = self.helper.get_yaml_items(directory)
        for item in items:
            kwargs = {'role': role, 'item': item}
            if item.startswith(role + self.config.PREFIX_SEPERATOR):
                self.passed('The variable {item} is correct prefixed in the role {role}'.format(**kwargs))
            else:
                self.failed('The variable {item} is not correct prefixed in the role {role}'.format(**kwargs))
