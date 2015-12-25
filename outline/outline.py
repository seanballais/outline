#!/usr/bin/python3

import sys
import getopt

def main(argv):
    # Handle the command line arguments
    scripts_location = ""
    config_file = ""
    project_name = ""

    try:
        opts, args = getopt.getopt(argv, "hvc:s:", ["help", "version",
                                                    "config=", "scripts"])

if __name__ == "__main__":
    self.main(sys.arg[1:])
