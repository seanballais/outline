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
        self.assertEqual(util.locate_project_name(["project", "-c"]), "project")
        self.assertEqual(util.locate_project_name(["-project", "-c"]), False)

if __name__ == "__main__":
    unittest.main()
