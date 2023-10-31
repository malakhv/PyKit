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

The module to working with version in "Semantic Versioning 2" format.

Author: Mikhail.Malakhov

"""

#--------------------------------------------------------------------------
# Version in "Semantic Versioning 2" format (XX.YY.ZZZ).
#--------------------------------------------------------------------------

""" Returns version code. """
def get_version_code(major = 0, minor = 0, patch = 0):
    return major * 100000 + minor * 1000 + patch
# END

""" Returns version name in "Semantic Versioning 2" format. """
def get_version_name(major = 0, minor = 0, patch = 0):
    return str(major) + '.' + str(minor) + '.' + str(patch)
# END

#--------------------------------------------------------------------------
