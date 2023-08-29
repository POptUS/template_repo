"""
A generic unittest test case template.

This template exists to aid in the creation of new test cases and should never
fail.
"""

import unittest

class TestTemplate(unittest.TestCase):
    def setUp(self):
        print("setUp() is an optional fixture that is automatically called before each test")

    def tearDown(self):
        print("tearDown() is an optional fixture that is automatically called after each test")

    def testNothing(self):
        self.assertTrue(True)
