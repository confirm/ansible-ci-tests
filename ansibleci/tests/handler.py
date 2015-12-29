# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ansibleci.test import Test
import os


class Handler(Test):
    '''
    Test to check if all notified handlers (i.e. ``notify:``) are available.

    The task ``notify:`` parameters will be looked up in all ``tasks/*`` files,
    while the handler ``name:`` parameters will be looked up in all
    ``handlers/*`` files.
    '''

    def run(self):
        '''
        Runs all tests defined in the config's ENABLED_TESTS list.
        '''
        self.roles = self.get_helper().get_roles()

        notifies = self.get_notifies()
        handlers = self.get_handlers()

        for role, notifies in notifies.iteritems():
            for notify in notifies:
                kwargs = {'role': role, 'notify': notify}
                if notify in handlers:
                    self.passed('Handler "{notify}" of role {role} found'.format(**kwargs))
                else:
                    self.failed('Handler "{notify}" of role {role} not found'.format(**kwargs))

    def get_notifies(self):
        '''
        Returns all task notifies in form of a dict, while the key is the role
        name and the value is the notified handler string.
        '''
        notifies = {}

        for name, path in self.roles.iteritems():
            dir_path      = os.path.join(path, 'tasks')
            role_notifies = self.get_helper().get_yaml_items(dir_path=dir_path, param='notify')
            if role_notifies:
                notifies[name] = role_notifies

        return notifies

    def get_handlers(self):
        '''
        Returns all handlers in a simple list.
        '''
        handlers = []

        for name, path in self.roles.iteritems():
            dir_path = os.path.join(path, 'handlers')
            handlers.extend(self.get_helper().get_yaml_items(dir_path=dir_path, param='name'))

        return handlers
