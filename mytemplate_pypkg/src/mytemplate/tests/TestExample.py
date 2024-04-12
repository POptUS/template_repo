"""
Package run_my_example example code in unittest TestCase wrapper for inclusion
in test suite
"""

import unittest

import mytemplate.examples


class TestExample(unittest.TestCase):
    def testExample(self):
        mytemplate.examples.run_my_example()
