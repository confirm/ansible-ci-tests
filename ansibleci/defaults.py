# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import os

#
# Ansible paths.
#

# Basedir which should point to an Ansible project.
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

# Roles directory paths, can be absolute or relative (to BASEDIR).
ROLES = [
    'roles/',
]

# Playbooks directory paths, can be absolute or relative (to BASEDIR).
PLAYBOOKS = [
    'plays/',
]

# A list with File extensions, which are used in the ansible project.
FILE_EXENTSIONS = [
    'yml',
    'yaml',
]

#
# A list of tests to run.
#

ENABLED_TESTS = [
    'ansibleci.tests.readme.Readme',
    'ansibleci.tests.handler.Handler',
    'ansibleci.tests.tag.Tag',
    'ansibleci.tests.deprecated.Deprecated',
]

#
# Settings for ansibleci.tests.readme.
#

# Name of the role's Readme file.
README_FILENAME = 'README.md'

# Should the default vars be checked?
README_CHECK_DEFAULTS = True

#
# Settings for ansibleci.tests.tag.
#

# Should the tag name be identical with the role name?
TAG_ROLE_NAME = True

#
# Settings for ansibleci.tests.deprecated.
#

# A list with deprecated directives.
DEPRECATED_DIRECTIVES = [
    'sudo',
    'sudo_user',
    'su',
    'su_user',
]
