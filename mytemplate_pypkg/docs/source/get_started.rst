Getting Started
===============

General Installations
---------------------
There should be at least three options for installing this package.  For
developer installations, refer to the :numref:`developers_guide:Developer
Environment`.

|pip| install |via| `PyPi`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _PyPi: https://pypi.org
.. _virtual environments: https://docs.python.org/3/library/venv.html

.. note:: This package is not in PyPi and, therefore, this method cannot be
    executed in practice

This is the preferred method for users who prefer |pip| installations over
direct use of local clones.

* Setup the python environment that will use the package (|eg| `virtual environments`_)
* Update |pip|, ``setuptools``, and ``wheel`` if necessary and desired
* Install this package by executing from any directory

.. code-block:: console

    $ which python
    $ python --version
    $ which pip
    $ pip --version
    $ pip install --upgrade mytemplate
    $ pip list

|pip| install |via| downloaded GitHub action `artifacts`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _artifacts: https://github.com/POptUS/template_repo/actions/runs/6005607898
.. _GitHub action: https://github.com/POptUS/template_repo/actions
.. _source distribution: https://packaging.python.org/en/latest/flow/#the-source-distribution-sdist
.. _prebuilt distribution: https://packaging.python.org/en/latest/flow/#the-built-distributions-wheels

This method might be useful to developers for testing/debugging or power users
who would like to use a specific version of the package not available through
``PyPi``.

* Click on the `GitHub action`_ associated with the commit whose package version
  is to be installed
* Download the artifacts of the python package to install
* Extract the artifact, confirm that it contains distributions (``*.tar.gz``
  is a `source distribution`_; ``*.whl`` is a `prebuilt distribution`_),
  and choose which to install
* Install this package by executing from any directory

.. code-block:: console

    $ pip install --upgrade </path/to/distribution to install>
    $ pip list

Manual source distribution installation |via| `setuptools`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _setuptools: https://setuptools.pypa.io/en/latest/index.html

This method might be useful for developers.  After activating your target
python and |pip|, execute

* ``cd </path/to/mytemplate_pypkg>``
* Test manually with python or |tox| (See :numref:`developers_guide:Developer Environment`)
* Install source distribution of the package by executing from the current
  working directory

.. code-block:: console

    $ python setup.py sdist
    $ pip install --upgrade dist/mytemplate-<version>.tar.gz
    $ pip list

where ``<version>`` is the version of the package to be installed.  This can be
determined by scanning the standard output generated when creating the
``sdist``.  Note that the ``--user`` install flag might be useful if installing
in a community system in which the python/|pip| are write-protected.

Installation Testing
--------------------

To test all installations, run

.. code-block:: console

    $ python
    >>> import mytemplate
    >>> mytemplate.__version__
    <version>
    >>> mytemplate.test()
        ...
    $ python -m pydoc mytemplate

where the output ``<version>`` should be identical to the value used during
installation.  Review the test output to confirm that all tests have passed.

For those who cloned the repository, installations can also be tested by running 

.. code-block:: console

    $ cd </path/to/clone>
    $ ./tools/test_mytemplate_installation.py

and inspecting information as well as test results for indicators of successful
installation.
