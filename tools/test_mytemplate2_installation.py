#!/usr/bin/env python

"""
Run the script with -h to obtain more information regarding the script.
"""

import inspect
import argparse
import importlib

from pathlib import Path

# ----- HARDCODED VALUES
# Exit codes so that this can be used in CI build server
_FAILURE = 1
_SUCCESS = 0


try:
    import mytemplate2
except ImportError as error:
    print()
    print(f"ERROR: {error.name} python package not installed")
    print()
    exit(_FAILURE)


def main():
    # Keep output compact so that package info is seen with each run
    DEFAULT_VERBOSITY = 1

    # ----- SPECIFY COMMAND LINE USAGE
    DESCRIPTION = "Return status of mytemplate2 python package full testing " \
                  + "as exit code for use with CI\n"
    VERBOSE_HELP = "Verbosity level of python unittest logging"
    parser = argparse.ArgumentParser(
                description=DESCRIPTION,
                formatter_class=argparse.RawTextHelpFormatter
             )
    parser.add_argument(
        "--verbose", "-v",
        type=int, choices=[0, 1, 2], default=DEFAULT_VERBOSITY,
        help=VERBOSE_HELP
    )

    # ----- GET COMMAND LINE ARGUMENTS
    args = parser.parse_args()
    verbosity_level = args.verbose

    # ----- PRINT VERSION INFORMATION
    pkg = importlib.metadata.distribution("mytemplate2")
    location = Path(inspect.getfile(mytemplate2)).parents[0]

    print()
    print("Name: {}".format(pkg.metadata["Name"]))
    print("Version: {}".format(pkg.metadata["Version"]))
    print("Summary: {}".format(pkg.metadata["Summary"]))
    print("Homepage: {}".format(pkg.metadata["Home-page"]))
    print("License: {}".format(pkg.metadata["License"]))
    print("Python requirements: {}".format(pkg.metadata["Requires-Python"]))
    print("Package dependencies: {}".format(pkg.metadata["Requires-Dist"]))
    print("Location: {}".format(location))
    print()

    # ----- RUN FULL TEST SUITE
    return _SUCCESS if mytemplate2.test(verbosity_level) else _FAILURE


if __name__ == "__main__":
    exit(main())
