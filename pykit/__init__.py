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

"""

Python Kit Library (PyKit)

The common library for Python projects. It contains useful utilities
and stuff.

"""

PYKIT_NAME = 'pykit';
PYKIT_TITLE = 'PyKit';

#--------------------------------------------------------------------------
# Library version in "Semantic Versioning 2" format (XX.YY.ZZZ).
# Please, keep it sync with setup.py.
#--------------------------------------------------------------------------

""" The major (XX) version's part. Available values 0..99. """
PYKIT_VERSION_MAJOR = 0

""" The minor (YY) version's part. Available values 0..99. """
PYKIT_VERSION_MINOR = 1

""" The patch (ZZZ) version's part. Available values 0..999. """
PYKIT_VERSION_PATCH = 0

""" Gets PyKit library version code. """
def pykit_version_code():
    return PYKIT_VERSION_MAJOR * 100000 + PYKIT_VERSION_MINOR * 1000
    + PYKIT_VERSION_PATCH
# END

""" Gets PyKit library version name. """
def pykit_version_name():
    return str(PYKIT_VERSION_MAJOR) + '.' + str(PYKIT_VERSION_MINOR) + '.'
    + str(PYKIT_VERSION_PATCH)
# END

#--------------------------------------------------------------------------
