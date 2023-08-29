"""
The wonderful and amazing do-nothing mytemplate package
"""

from importlib.metadata import version

__version__ = version("mytemplate")

# functions
from .compute import compute

# constants
from .constants import config

# ----- Python unittest-based test framework
# Used for automatic test discovery
from .load_tests import load_tests

# Allow users to run full test suite as mytemplate.test()
from .test import test
