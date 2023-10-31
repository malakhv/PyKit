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

from setuptools import find_packages, setup
#from . import pykit

def long_description():
    with open("README.md") as file:
        return file.read()

#--------------------------------------------------------------------------
# Python package
#--------------------------------------------------------------------------

setup (

    name = "pykit",
    version = "0.1.0",

    description="The common library for Python projects",
    long_description = long_description(),
    long_description_content_type = "text/markdown",

    author = "Mikhail Malakhov",
    author_email = "malakhv@gmail.com",
    
    url = "https://github.com/malakhv/PyKit",
    project_urls = {
        "GitHub Project": "https://github.com/malakhv/PyKit",
        "Issue Tracker": "https://github.com/malakhv/PyKit/issues",
    },

    packages=find_packages(
        include = ["pykit", "pykit.*"],
    ),

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    license="Apache 2.0",
)

#--------------------------------------------------------------------------
