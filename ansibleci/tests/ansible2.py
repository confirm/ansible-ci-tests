# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ansibleci.test import Test
import os


class Ansible2(Test):
    '''
    Test to check if Ansible Project is ready for Ansible 2.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        self.plays = self.helper.get_playbooks()

        deprectated_directives = 'sudo', 'su_user', 'su'

        for directive in deprectated_directives:
            self.test_deprecated_directives(directive=directive)


    def test_deprecated_directives(self, directive):
        '''
        Tests if there are deprecated directives used in the playbook files.
        '''
        for playbook,path in self.plays.iteritems():

            kwargs = {
                'directive': directive,
                'playbook': playbook,
            }

            for item in self.helper.read_yaml(path):
                if directive in item:
                    found = True
                else:
                    found = False

            if found:
                self.failed('Directive {directive} exists in the playbook {playbook}'.format(**kwargs))
            else:
                self.passed('Directive {directive} exists not in the playbook {playbook}'.format(**kwargs))
