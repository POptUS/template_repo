"""
A generic unittest test case template.

This template exists to aid in the creation of new test cases and should never
fail.
"""

import unittest


class TestTemplate(unittest.TestCase):
    def setUp(self):
        msg = "setUp() is an optional fixture that is automatically called " \
              "before each test"
        print(msg)

    def tearDown(self):
        msg = "tearDown() is an optional fixture that is automatically " \
              "called after each test"
        print(msg)

    def testNothing(self):
        self.assertTrue(True)
