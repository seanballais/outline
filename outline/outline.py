#!/usr/bin/python3

import sys
import getopt

import help
import info

def main(argv):
    # Handle the command line arguments
    scripts_location = ""
    config_file = ""
    project_name = ""

    if "-h" or "--help" in argv or not argv:
        help.help()
    else if argv[0] == "-V" or argv[0] == "--version":
        info.info()
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
