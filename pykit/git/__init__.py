#
# Copyright (C) 1996-2023 Mikhail Malakhov <malakhv@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.
#
# See the License for the specific language governing permissions
# and limitations under the License.
#

#--------------------------------------------------------------------------
# This file is a part of PyKit project.
# Created: 04.11.2023
# Author: Mikhail.Malakhov
#--------------------------------------------------------------------------

"""

Python Kit Library (PyKit)

The module to working with Git.

Author: Mikhail.Malakhov

"""

from .. import process as _ps

#--------------------------------------------------------------------------
# Common git tools
#--------------------------------------------------------------------------

""" Executes Git command for specified path. """
def git_for_path(git_cmd, *args, path = '.', compact_out = False, \
        print_out = True):
    git_args = ['-C' , path, git_cmd]
    if args : git_args.extend(args)
    out = _ps.exec('git', *git_args, silent=(not print_out), \
        out_keep_empty_lines= (not compact_out))
    if print_out and (out != None): print(out)
# END

#--------------------------------------------------------------------------
# Git commands
#--------------------------------------------------------------------------

""" Executes git command for specified directory: git status. """
def git_status(path = '.', print_out = True, compact_out = False):
    return git_for_path('status', path = path, compact_out = compact_out, \
        print_out = print_out)
# END

""" Executes git command for specified directory: git fetch. """
def git_fetch(path = '.', print_out = True, compact_out = False):
    return git_for_path('fetch', path = path, compact_out = compact_out, \
        print_out = print_out)
# END

""" Executes git command for specified directory: git pull. """
def git_pull(path = '.', print_out = True, compact_out = False):
    return git_for_path('pull', path = path, compact_out = compact_out, \
        print_out = print_out)
# END

""" Executes git command for specified directory: git push. """
def git_push(path = '.', print_out = True, compact_out = False):
    return git_for_path('push', path = path, compact_out = compact_out, \
        print_out = print_out)
# END

""" Executes git command for specified directory: git clone. """
def git_clone(host, name, path = '.', print_out = True, \
        compact_out = False):
    git_args = [host + '/' + name + '.git']
    return git_for_path('clone', *git_args, path = path, \
        compact_out = compact_out, print_out = print_out)
# END

#--------------------------------------------------------------------------
# Git config
#--------------------------------------------------------------------------

""" Working with local Git config: set. """
def git_config_set(path, name, value) :
    if not name or not value :
        print("git_config_set - Illegal Arguments..."); return
    config = ['config', '--local', name, value]
    git_for_path(path, *config)
# END

""" Working with local Git config: get. """
def git_config_get(path, name = '') :
    config = ['config', '--local']
    if name :
        config.extend(['--get', name])
    else:
        config.append('-l')
    return git_for_path(path, *config)
# END

#--------------------------------------------------------------------------
# END
#--------------------------------------------------------------------------
