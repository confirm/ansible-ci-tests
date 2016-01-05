# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ansibleci.test import Test
import os


class Deprecated(Test):
    '''
    Test to check if deprecated directives are used.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        self.config = self.get_config()
        self.helper = self.get_helper()
        self.directives = self.config.DEPRECATED_DIRECTIVES

        self.test_deprecated_directives(self.helper.get_playbook_yaml_files())
        self.test_deprecated_directives(self.helper.get_role_task_yaml_files())

    def initialize_counter(self):
        '''
        Initialize a counter for the directives.
        '''
        counter = {}
        for directive in self.directives:
            counter[directive] = 0
        return counter

    def test_deprecated_directives(self, files):
        '''
        Tests if there are deprecated directives used in the yaml files.
        '''
        for path in files:
            content = self.helper.read_yaml(path)

            counter = self.initialize_counter()

            for item in content:
                for directive in self.directives:
                    if directive in item:
                        counter[directive] += 1

            for directive in self.directives:
                count = counter[directive]
                kwargs = {
                    'name': path,
                    'directive': directive,
                    'count': count
                }
                if count == 0:
                    self.passed('Directive {directive} exists not in the file {name}'.format(**kwargs))
                elif count == 1:
                    self.failed('Directive {directive} exists {count} time in the file {name}'.format(**kwargs))
                else:
                    self.failed('Directive {directive} exists {count} times in the file {name}'.format(**kwargs))
