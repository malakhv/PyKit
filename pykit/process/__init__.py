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
# Created: 31.10.2023
# Author: Mikhail.Malakhov
#--------------------------------------------------------------------------

"""

Python Kit Library (PyKit)

The module to working with external processes.

Author: Mikhail.Malakhov

"""
import subprocess
from subprocess import CalledProcessError

#--------------------------------------------------------------------------
# Execute external process/command.
#--------------------------------------------------------------------------

""" Executes specified process/command with parameters. """
def exec(proc, *args, shell = True, silent = False,  out_prefix = '', \
    out_postfix = '', out_keep_empty_lines = True):

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
    try:
        process = subprocess.run(cmd, shell = shell, check = True, \
            capture_output = custom_out, text = custom_out)
    except CalledProcessError as e:
        if (not custom_out):
            print(e.stderr)
        else:
            result = e.stderr

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

    if (custom_out):
        return result
    else:
        return None
# END

#--------------------------------------------------------------------------
