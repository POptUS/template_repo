from pathlib import Path

from .subA import load_tests as load_tests_subA
from .subB import load_tests as load_tests_subB


def load_tests(loader, *_):
    """
    This function implements the load_tests protocol of the python unittest
    package.  In particular, it gathers into a single test suite all tests in
    the overall package so that clients using the package don't need to know
    where the tests are or what patterns they need to look for to find all
    tests.

    This function doesn't assume that it knows how to find all tests in
    sub-packages.  Rather, it uses the load_tests functions in each of those to
    gather tests.

    Developers of new sub-packages must manually integrate their sub-package
    into this function.

    Developers and users can run tests using this indirectly via
                         python -m unittest mytemplate

    Parameters:
        loader - the unittest.TestLoader instance doing the loading
    """
    here_dir = Path(__file__).resolve().parent
    start_dir = here_dir.joinpath("tests")

    print()
    print(f"Discover tests in {start_dir}")
    suites = loader.discover(
        start_dir=str(start_dir),
        top_level_dir=str(here_dir),
        pattern="Test*.py"
    )
    suites = load_tests_subA(loader, suites, None)
    suites = load_tests_subB(loader, suites, None)
    print()

    return suites
