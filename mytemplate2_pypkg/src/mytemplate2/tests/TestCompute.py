"""
Unit test compute function
"""

import unittest

import mytemplate2 as myt2


class TestCompute(unittest.TestCase):
    def testSomething(self):
        self.assertEqual(-250.0, myt2.compute(5.0))
