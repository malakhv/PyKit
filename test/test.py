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
# Script to test PyKit library.
#
# Created: 31.10.2023
# Author: Mikhail.Malakhov
#
# This file is a part of PyKit project.
#--------------------------------------------------------------------------

import pykit
from pykit import process

#--------------------------------------------------------------------------
# Script entry point
#--------------------------------------------------------------------------

if __name__ == '__main__':

    # PyKit version
    print(pykit.PYKIT_TITLE, 'version:', pykit.pykit_version_name(),
        '(' + str(pykit.pykit_version_code()) + ')')
    
    # PWD
    print(pykit.pwd())

    # Process
    print()
    str = process.exec('git', 'status', out_prefix = '-----GIT STATUS -----', \
        out_postfix = '---------------------', shell=False, \
            out_keep_empty_lines=True)
    print(str)

#--------------------------------------------------------------------------
