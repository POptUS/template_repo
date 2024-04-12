def load_tests(loader, suite, _):
    """
    This function implements the ``load_tests`` protocol of the python unittest
    package.

    Developers and users can run tests using this indirectly |via|::

                         python -m unittest mytemplate

    to run as part of the package's full suite or |via|::

                  python -m unittest mytemplate.subA.examples

    to run alone.

    :param loader: ``unittest.TestLoader`` instance doing the loading
    :param suite: test suite being built at the time of call to this function
    :return: Given suite with all ``examples`` tests added in
    """
    # The examples tests are in ../tests and should be added to the suite by
    # that folder.
    return suite
