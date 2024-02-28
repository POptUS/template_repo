"""
The wonderful and amazing do-nothing mytemplate package
"""

from importlib.metadata import version

__version__ = version("mytemplate")

# helpers needed for following imports
from .__load_config_from_json import __load_config_from_json

# functions
from .compute import compute

# ----- Python unittest-based test framework
# Used for automatic test discovery
from .load_tests import load_tests

# Allow users to run full test suite as mytemplate.test()
from .test import test

# ----- Module data constants
#: My module configuration data
config = __load_config_from_json()
