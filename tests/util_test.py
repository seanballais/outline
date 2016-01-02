#!/usr/bin/python3
import os
import sys
import unittest

if os.path.split(os.getcwd())[1] == "tests":
    sys.path.append("../outline")
else:
    sys.path.append("outline")

import util

class UtilTest(unittest.TestCase):
    def test_locate_project_name(self):
        test_list = ["project", "-c"]
        self.assertEqual(util.locate_project_name(test_list), "project")

if __name__ == "__main__":
    unittest.main()
