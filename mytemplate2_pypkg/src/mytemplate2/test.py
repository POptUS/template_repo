import unittest

from mytemplate2 import load_tests


def test(verbosity=1):
    """
    Run the full set of tests in the package with results presented to caller
    using a simple text interface.

    This is included so that users can test their actual installation directly
    or record test results in jupyter notebook output for reproducibility via
                              mytemplate2.test()

    Parameters
        verbosity - the verbosity level to pass to the unittest TestRunner
    Return
        True if all tests in package passed; False, otherwise.
    """
    loader = unittest.TestLoader()
    suite = load_tests(loader, None, None)
    result = unittest.TextTestRunner(verbosity=verbosity).run(suite)

    return result.wasSuccessful()
