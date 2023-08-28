"""
Unit test of compute_c function
"""

import unittest

import mytemplate2.subC as myt2C


class TestComputeC(unittest.TestCase):
    def testSomething(self):
        self.assertEqual(27.0, myt2C.compute_c(3.0))
