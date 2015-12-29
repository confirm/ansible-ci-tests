# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ansibleci.test import Test
import os


class Tag(Test):
    '''
    Test to check if all tasks are tagged properly with the ``tags:`` parameter.

    If the ``TAG_ROLE_NAME`` config flag is set to ``True``, the test will also
    make sure that all tasks are tagged with the role's name.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        config = self.get_config()
        helper = self.get_helper()

        for name, path in helper.get_roles().iteritems():

            dir_path = os.path.join(path, 'tasks')
            items    = helper.get_yaml_items(dir_path)

            for item in items:

                kwargs = {
                    'task': helper.get_item_identifier(item),
                    'role': name
                }

                if 'tags' in item:
                    if config.TAG_ROLE_NAME:
                        tags = item['tags']
                        if (isinstance(tags, list) and name in tags) or tags == name:
                            self.passed('Task "{task}" in role {role} is tagged with the role name'.format(**kwargs))
                        else:
                            self.failed('Task "{task}" in role {role} is not tagged with the role name'.format(**kwargs))
                    else:
                        self.passed('Task "{task}" in role {role} is tagged'.format(**kwargs))
                else:
                    self.failed('Task "{task}" in role {role} is untagged'.format(**kwargs))
