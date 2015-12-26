#!/usr/bin/python3

import sys

import info
import util

def main(argv):
    # Handle the command line arguments
    scripts_location = "~/.outline/scripts/"
    config_file = ""
    project_name = ""
    verbose = False
    if "-h" or "--help" in argv or not argv:
        info.help() # I need somebody
    else if argv[0] == "-V" or argv[0] == "--version":
        info.info()
    else:
        # Check for mistakes in the arguments first
        if util.elem_occurences_in_list(argv, "-c") > 1 or
           util.elem_fragment_occurences_in_list(argv, "--config=" > 1 or
           util.elem_occurences_in_list(argv, "-s") > 1 or
           util.elem_fragment_occurences_in_list(argv, "--scripts=") > 1:
           info.help() # Not just anybody
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
