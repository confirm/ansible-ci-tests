# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ansibleci.test import Test
import os


class Readme(Test):
    '''
    Test to check if all roles have a Readme file in place.

    If the ``README_CHECK_DEFAULTS`` config flag is set to ``True``, then it
    will also check if the role's default variables (i.e. ``defaults/*``) are
    mentioned in the role's Readme file.

    The name of the Readme file is controled with the ``README_FILENAME``
    config variable.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        roles = self.get_helper().get_roles()
        self.test_readme(roles)

    def test_readme(self, roles):
        '''
        Tests the existence of role's README files and if the README files
        exists it will call the test_defaults() for each role.
        '''
        readme_filename = self.get_config().README_FILENAME

        for name, path in roles.iteritems():
            readme = os.path.join(path, readme_filename)
            if os.path.isfile(readme):
                self.passed('Readme file for role {role} is existing'.format(role=name))
                self.test_defaults(name=name, path=path, readme=readme)
            else:
                self.failed('Readme file for role {role} is missing'.format(role=name))

    def test_defaults(self, name, path, readme):
        '''
        Tests if all variables in the defaults/main.yml are documented in the
        role's Readme file.
        '''
        if not self.get_config().README_CHECK_DEFAULTS:
            return

        defaults = os.path.join(path, 'defaults/main.yml')

        if not os.path.isfile(defaults):
            return

        with open(readme, 'r') as f:
            readme_content = f.read()

        for var in self.get_helper().read_yaml(defaults).keys():
            kwargs = {'var': var, 'role': name}
            if var in readme_content:
                self.passed('Default variable {var} of role {role} is mentioned in role\'s Readme file'.format(**kwargs))
            else:
                self.failed('Default variable {var} of role {role} is not mentioned in role\'s Readme file'.format(**kwargs))
