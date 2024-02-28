"""
Package run_my_example example code in unittest TestCase wrapper for inclusion
in test suite
"""

import unittest

import mytemplate.subA.examples


class TestExample(unittest.TestCase):
    def testExample(self):
        mytemplate.subA.examples.run_my_example()
