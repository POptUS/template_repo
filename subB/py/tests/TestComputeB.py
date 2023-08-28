"""
Unit test of the compute_b function
"""

import unittest

import mytemplate.subB as mytB


class TestComputeB(unittest.TestCase):
    def testSomething(self):
        self.assertEqual(27.0, mytB.compute_b(3.0))
