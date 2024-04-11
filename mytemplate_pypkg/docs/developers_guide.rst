Developers's Guide
==================

Developer Environment
---------------------

Development with `tox`_
^^^^^^^^^^^^^^^^^^^^^^^
.. _tox: https://tox.wiki/en/latest/index.html

The coverage reports for this package are managed with |tox|, which can be used
for CI work among other work.  However, the same |tox| setups can be used by
developers if so desired.  This can be useful since |tox| will automatically
setup and manage dedicated virtual environments for the developer.  The
following guide can be used to setup |tox| as a command line tool on an
individual platform in a dedicated, minimal virtual environment and is based on
a `webinar <https://www.youtube.com/watch?v=PrAyvH-tm8E>`_ by Oliver
Bestwalter.  I appreciate his solution as there is no need to activate the
virtual environment in order to use |tox|.

.. note::
    Developers that would like to use |tox| should learn about the tool so
    that, at the very least, they understand the difference between running
    ``tox`` and ``tox -r``.

To create a python virtual environment based on a desired python dedicated to
hosting |tox|, execute some variation of

.. code-block:: console

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

To avoid the need to activate ``.toxbase``, we setup |tox| in ``PATH`` for
use across all development environments that we might have on our system. In
the following, please replace ``.bash_profile`` with the appropriate shell
configuration file and tailor the following to your needs.

.. code-block:: console

    $ mkdir $HOME/local/bin
    $ ln -s $HOME/.toxbase/bin/tox $HOME/local/bin/tox
    $ vi $HOME/.bash_profile (add $HOME/local/bin to PATH)
    $ . $HOME/.bash_profile
    $ which tox
    $ tox --version

If the environment variable ``COVERAGE_FILE`` is set, then this is the coverage
file that will be used with all associated work.  If it is not specified, then
the coverage file is ``.coverage_mytemplate``.

No work will be carried out by default with the calls ``tox`` and ``tox -r``.

The following commands can be run from the directory that contains this
package's |tox| configuration file

.. code-block:: console

    /path/to/mytemplate_pypkg/tox.ini

* ``tox -r -e coverage``

  * Execute the full test suite for the package and save coverage results to
    the coverage file
  * The test runs the package code in the local clone rather than code
    installed into python so that coverage results accessed through web
    services such as Coveralls are clean and straightforward
* ``tox -r -e nocoverage``

  * Execute the full test suite for the package using the code installed into
    python
* ``tox -r -e oldest``

  * Execute the full test suite for the package using the code installed into
    python but using the oldest allowable version of all dependencies
* ``tox -r -e subA``

  * Execute the test suite for the ``subA`` sub-package only using the code
    installed into python
* ``tox -r -e subB``

  * Execute the test suite for the ``subB`` sub-package only using the code
    installed into python
* ``tox -r -e report``

  * It is intended that this be run after or with ``coverage``
  * Display a code coverage report for the package's full test suite and
    generate an HTML version of the report
* ``tox -r -e check``

  * This is likely only useful for developers working on a local clone
  * Run several checks on the code to report possible issues
  * No files are altered automatically by this task
* ``tox -r -e html``

  * Generate and render the package's documentation locally in HTML
* ``tox -r -e pdf``

  * Generate and render the package's documentation locally as a PDF file

Additionally, you can run any combination of the above such as ``tox -r -e
report,coverage``.

Manual Developer Testing
^^^^^^^^^^^^^^^^^^^^^^^^
It is possible to test manually outside of |tox|, which could be useful for
testing at the level of a single test.

The following example shows how to run only a single test case using the
``coverage`` virtual environment setup by |tox|.

.. code-block:: console

    $ cd /path/to/mytemplate_pypkg
    $ tox -r -e coverage
    $ . ./.tox/coverage/bin/activate
    $ which python
    $ python --version
    $ pip list
    $ python -m unittest mytemplate.subA.tests.TestComputeA

Adding a New Subpackage to ``mytemplate``
-----------------------------------------
.. _subA: https://github.com/POptUS/template_repo/tree/main/subA

* Add new subpackage to the root of the repo in accord with the |poptus|
  repository requirements (|eg| `subA`_)
* Increment ``VERSION`` appropriately
* Add in the new subpackage implementation as symlinks in the correct
  subdirectory
* Update ``load_tests.py`` in the main package so that it builds a suite that
  includes the tests of the subpackage
* Update ``README.md`` and all other documentation as needed
* Adapt ``setup.py``

  * Update or expand all requirements as needed
  * Add test and package data in new subpackage to ``package_data`` if any
  * Update all other metadata as needed
* Update ``tox.ini``

  * Add a new testenv in ``tox.ini`` dedicated to the new subpackage if so
    desired
  * Synchronize python version information to version changes made in
    ``setup.py`` (if any)
* Do local testing with |tox| if so desired
* Synchronize python version information in GitHub CI actions to version changes
  made in ``setup.py`` (if any)
* Commit, push, and check associated GitHub CI action logs to see if constructed
  and integrated correctly
