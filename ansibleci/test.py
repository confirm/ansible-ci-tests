# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class Test(object):
    '''
    This is the abstract class for all tests, which means all concrete test
    classes must inherit from this class.
    '''

    def __init__(self, runner):
        '''
        Class constructor which sets the runner instance.
        '''
        self.runner     = runner
        self.config     = runner.config
        self.helper     = runner.helper
        self.has_passed = True

    def get_runner(self):
        '''
        Returns the Runner instance which has called / instanced us.
        '''
        return self.runner

    def get_config(self):
        '''
        Returns the Runner's Config instance, which can be used to access
        configuration params.
        '''
        return self.config

    def get_helper(self):
        '''
        Returns the Runner's Helper instance, which can be used to access
        common used methods.
        '''
        return self.helper

    def passed(self, message):
        '''
        Marks a (sub-)test as passed.
        This will not change the result of the whole test.
        '''
        self.runner.logger.test_passed(message)

    def failed(self, message):
        '''
        Marks a (sub-)test as failed.
        This will change the result of the whole test to FAILED.
        '''
        self.runner.logger.test_failed(message)
        self.has_passed = False

    def _run(self):
        '''
        Runs the test and returns a boolean if the test has passed or not.
        '''
        if not hasattr(self, 'run'):
            raise AttributeError('Test {test} has no run() method implemented'.format(test=self.__class__.__name__))

        self.run()

        return self.has_passed
