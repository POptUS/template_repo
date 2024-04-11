## Repository Status

|             | Badges |
|:-----------:|:------:|
| General     | ![GitHub](https://img.shields.io/github/license/POptUS/template_repo) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |
| Test Status | ![GitHub Action CI](https://github.com/POptUS/template_repo/actions/workflows/github-ci-action.yml/badge.svg) [![Coverage Status](https://coveralls.io/repos/github/POptUS/template_repo/badge.svg?branch=main)](https://coveralls.io/github/POptUS/template_repo?branch=main) |

## General Information
This repository is a template and testbed for setting up new repositories in the
[POptUS organization](https://github.com/POptUS).  A concrete example of such a repository is
[IBCDFO](https://github.com/POptUS/IBCDFO/tree/main), which groups together similar optimization tools.
The following is a set of requirements that motivated the construction of this
template and which all other POptUS repositories should satisfy so that POptUS users
and developers can benefit from a common [look and feel](https://en.wikipedia.org/wiki/Look_and_feel) across all repos.  New POptUS
repos can be [seeded from this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

#### General Requirements
* Each distinct tool to be included in the repository shall (e.g., [subA](https://github.com/POptUS/template_repo/tree/main/subA),
  [subB](https://github.com/POptUS/template_repo/tree/main/subB)) be included in the root of the repository in a folder named after the
  tool.
* Each implementation of a tool shall be included in a dedicated folder in the
  tool's main folder with its name adhering to the convention
  * `m` - for a MATLAB implementation (e.g., [subA/m](https://github.com/POptUS/template_repo/tree/main/subA/m))
  * `py` - for a Python implementation (e.g., [subA/py](https://github.com/POptUS/template_repo/tree/main/subA/py))
  * Conventions for other languages __TBD__
* Users of the code in the repository shall be able to use the code correctly by
  cloning the repository and setting appropriate path variables correctly based
  on the languages of each tool that they plan to use.
* All public python packages shall be uploaded to [PyPi](https://pypi.org) so that users can choose
  to use the code via installation with pip and without having to clone the repository.
* This repository shall be setup so that it can host as many python packages as
  desired (e.g., [mytemplate_pypkg](https://github.com/POptUS/template_repo/tree/main/mytemplate_pypkg) and
  [mytemplate2_pypkg](https://github.com/POptUS/template_repo/tree/main/mytemplate2_pypkg)).  The python code
  related to individual tools to be included in a package shall __not__ be
  developed directly within the python package's folder hierarchy, but rather in
  accord with the above requirements.  Inclusion within the package shall be
  accomplished by [symbolic links](https://en.wikipedia.org/wiki/Symbolic_link)
  (e.g., [mytemplate_pypkg/src/mytemplate/subA](https://github.com/POptUS/template_repo/blob/main/mytemplate_pypkg/src/mytemplate/subA)).
* The repository shall be setup so that all tests in the repository regardless
  of language can be run via a [GitHub CI Action](https://github.com/POptUS/template_repo/blob/main/.github/workflows/github-ci-action.yml)
  and potentially through private build servers.
* The repository shall be setup so that coverage of all code in python packages
  can be determined as a single coverage result with coverage results published as
  [GitHub Action artifacts](https://github.com/POptUS/template_repo/actions/runs/6005607898).
  and via coverage web server interfaces (e.g., [Coveralls](https://coveralls.io/github/POptUS/template_repo)).
* The repository shall be setup so that tested distributions of all python packages are available as
  [GitHub Action artifacts](https://github.com/POptUS/template_repo/actions/runs/6005607898).

#### Python-specific Requirements
* All python packages shall be structured in accord with the [src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout),
  with tests in the package (e.g., [mytemplate_pypkg/src/mytemplate/tests](https://github.com/POptUS/template_repo/tree/main/mytemplate_pypkg/src/mytemplate/tests) and
  [mytemplate_pypkg/src/mytemplate/subA/tests](https://github.com/POptUS/template_repo/tree/main/subA/py/tests)).
  Detailed information regrading the benefits of the src layout [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/).
* All python packages shall provide access to their version information via the
  command `<package>.__version__`.  While each package is free to determine
  their own versioning scheme, note that
  [semantic versioning](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/?highlight=version#semantic-versioning-preferred)
  is the preferred scheme.  For information on providing the version
  information, see the discussion
  [here](https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version).
  In this repo we use a dedicated [`VERSION`](https://github.com/POptUS/template_repo/blob/main/mytemplate_pypkg/VERSION) file coupled with
  [`setup.py`](https://github.com/POptUS/template_repo/blob/main/mytemplate_pypkg/setup.py)
  and [`__init__.py`](https://github.com/POptUS/template_repo/blob/main/mytemplate_pypkg/src/mytemplate/__init__.py). 
* All python packages shall have integrated automatic unit testing that can be
  run within python via the command `<package>.test()` so that actual
  installations can be tested and test results can be recorded in jupyter
  notebooks for traceability.

#### MATLAB-specific Requirements
* __TBD__

## Developer Information
The python packages in this repository and the management of coverage reports
for the full repository are managed with
[tox](https://tox.wiki/en/latest/index.html), which can be used for CI work
among other work.  However, the same `tox` setups can be used by developers if
so desired.  This can be useful since `tox` will automatically setup and manage
dedicated virtual environments for the developer.  The following guide can be
used to setup `tox` as a command line tool on an individual platform in a
dedicated, minimal virtual environment and is based on the a
[webinar](https://www.youtube.com/watch?v=PrAyvH-tm8E) by Oliver Bestwalter.  I
appreciate his solution as there is no need to activate the virtual environment
in order to use `tox`.

Developers that would like to use `tox` should learn about the tool so that, at
the very least, they understand the difference between running `tox` and `tox
-r`.

To create a python virtual environment based on a desired python dedicated to
hosting `tox`, execute some variation of
```
$ cd
$ deactivate (to deactivate the current virtual environment if you are in one)
$ /path/to/desired/python --version
$ /path/to/desired/python -m venv $HOME/.toxbase
$ ./.toxbase/bin/pip list
$ ./.toxbase/bin/python -m pip install --upgrade pip
$ ./.toxbase/bin/pip install --upgrade setuptools
$ ./.toxbase/bin/pip install tox
$ ./.toxbase/bin/tox --version
$ ./.toxbase/bin/pip list
```

To avoid the need to activate `.toxbase`, we setup `tox` in `PATH` for use
across all development environments that we might have on our system. In the
following, please replace `.bash_profile` with the appropriate shell
configuration file and tailor to your needs.
```
$ mkdir $HOME/local/bin
$ ln -s $HOME/.toxbase/bin/tox $HOME/local/bin/tox
$ vi $HOME/.bash_profile (add $HOME/local/bin to PATH)
$ . $HOME/.bash_profile
$ which tox
$ tox --version
```

For information on using `tox` with a particular python package refer to the
`README.md` in the root folder of each package (e.g.,
[mytemplate_pypkg](https://github.com/POptUS/template_repo/blob/main/mytemplate_pypkg/README.md)).

## Using `tox` for Global Coverage Tasks
The python environments setup and managed at the root level of this repository
are for working globally with all coverage results generated independently by
testing individual code units in the repository.  In particular, it can be used
to combine these into a single file for generating global coverage reports.  As
such, this is a `tox` tool layer that requires advanced manual effort.  Its
primary use is with CI for
[automated report generation](https://github.com/POptUS/template_repo/blob/main/.github/workflows/github-ci-action.yml).

To use this layer, learn about and setup `tox` as described above.

No work will be carried out by default with the calls `tox` and `tox -r`.

The following commands can be run from the directory that contains this
`tox.ini`.
* `tox -r -e aggregate -- <coverage files>`
  * Combine all given `coverage.py` coverage files into the file `.coverage`
    located in the same directory as `tox.ini`
  * For best results, none of the given files should be named `.coverage`
  * Preserve the original coverage files
* `tox -r -e report`
  * It is intended that this be run after or with `aggregate`
  * Output a report and generate an HTML report for the aggregated coverage results
* `tox -r -e coveralls`
  * This is likely only useful for CI solutions
  * It is intended that this be run after or with `aggregate`
  * Send the aggegrated coverage report to Coveralls

Additionally, you can run any combination of the above such as
```
tox -r -e report,coveralls,aggregate -- <coverage files>
```
Note that `tox` will correctly and automatically run `aggregate` before the others.

## Adding a New Python Package
* Add all subpackage implementations to be included in the package to the root of the repo in accord with the above requirements (e.g., [subA](https://github.com/POptUS/template_repo/tree/main/subA))
* Create a new python package in the root of the repo based on the structure of [mytemplate_pypkg](https://github.com/POptUS/template_repo/tree/main/mytemplate_pypkg)
* Add in all subpackage implementations as symlinks in the correct subdirectory
* Adapt the contents of `load_tests.py` in the main directory of the new package so
  that it builds a suite that includes tests in the main package as well as the tests of all subpackages
* Set `VERSION` to the desired starting version
* Rewrite the `README.md` file for the new package
* Adapt the contents of `setup.py` to the new package
* Adapt the contents of `tox.ini` to the new package
* Do local testing with `tox` if so desired
* Add a `test_*_installation.py` script in the `tools` folder
* Incorporate the package into the [Python code check script](tools/check_python_code.sh)
* Incorporate the package into the [GitHub CI TestPyPkg](.github/workflows/github-ci-testPyPkgs.yml)
* Commit, push, and check associated GitHub CI actions' logs to see if constructed and integrated correctly
