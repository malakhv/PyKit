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

#-------------------------------------------------------------------------------
# Script to test PyKit library.
#
# Created: 31.10.2023
# Author: Mikhail.Malakhov
#
# This file is a part of PyKit project.
#-------------------------------------------------------------------------------

import pykit
from pykit import process
from pykit import git

import subprocess as _sp
from subprocess import CalledProcessError as _cpe

from os.path import abspath as _ap
from os import getcwd as _cwd

#-------------------------------------------------------------------------------
# Present Working Directory
#-------------------------------------------------------------------------------

""" Returns present working directory. """
def pwd():
    return _ap(_cwd())
# END

#-------------------------------------------------------------------------------
# Execute external process/command
#-------------------------------------------------------------------------------

""" Executes specified process/command with parameters. """
def exec(proc, *args, shell = False, silent = False,  out_prefix = '', \
        out_postfix = '', out_keep_empty_lines = True):

    result = ''

    # Prepare command
    cmd = [proc]
    if args : cmd.extend(args)

    # Want to use default output?
    custom_out = silent or (not out_keep_empty_lines)

    # Output prefix?
    if out_prefix:
        if (not custom_out):
            print(out_prefix)
        else:
            result = out_prefix + '\n'

    # Call
    process = None
    try:
        process = _sp.run(cmd, shell = shell, check = True, \
            capture_output = custom_out, text = custom_out)
    except _cpe as e:
        if (not custom_out):
            print(e.stderr)
        else:
            result = e.stderr
        return

    if (custom_out):
        result += process.stdout

    if (not out_keep_empty_lines):
        result = result.replace('\n\n','\n')

    # Output postfix?
    if (out_postfix):
        if (not custom_out):
            print(out_postfix)
        else:
            result += '\n' + out_postfix

    # Need a result?
    if (custom_out):
        return result
    else:
        return None

# END

#-------------------------------------------------------------------------------
# Script entry point
#-------------------------------------------------------------------------------

if __name__ == '__main__':

    # PyKit version
    print(pykit.PYKIT_TITLE, 'version:', pykit.pykit_version_name(),
        '(' + str(pykit.pykit_version_code()) + ')')
    
    # PWD
    print(pykit.pwd())
    print(pwd())

    # Process
    print()
    out = process.exec('git', 'status', out_keep_empty_lines=True, silent=False)
    #out = _sp.call(['git', 'status'])
    if (out) : print(out)


    # Git
    #print('-----------------------')
    #print('REPO: PyKit')
    #print('-----------------------')
    #out = git.git_status()
    #if (out) : print(out)

    # Git
    #print()
    #print()
    #print('-----------------------')
    #print('REPO: PascalKit')
    #print('-----------------------')
    #out = git.git_status()
    #if (out) : print(out)
#-------------------------------------------------------------------------------
