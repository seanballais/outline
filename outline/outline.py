#!/usr/bin/python3

import sys

import info
import util
import skeleton_creator
import run_plugins

def main(argv):
    # Handle the command line arguments
    # We're all set. Time to configure them settings
    args = {
        "project_name": "",
        "scripts": "",
        "config_file": "",
        "verbose": False,
    }
    if "-h" in argv or "--help" in argv or not argv:
        info.help() # I need somebody
    elif argv[0] == "-V" or argv[0] == "--version":
        info.info()
    else:
        # Check for mistakes in the arguments first
        if not util.arguments_valid(argv):
            sys.exit(2)

        if (argv.count("-c") > 1 or
            argv.count("-s") > 1 or
            argv.count("-v") > 1 or
            argv.count("--verbose") or
            util.fragment_count_in_list(argv, "--config=") > 1 or
            util.fragment_count_in_list(argv, "--scripts=") > 1 or
            not util.project_name_specified(argv)):
            info.help() # Not just anybody
            sys.exit(2)

        if not util.locate_project_name(argv):
            info.help() # You know I need somebody, help
            sys.exit(2)

        if not util.locate_config_file(argv):
            info.help() # !
            sys.exit(2)

        if not util.locate_scripts_folder(argv):
            info.help() # When I was younger, so much younger than today
            sys.exit(2)

        # Finished validating the passed arguments
        args["project_name"] = util.locate_project_name(argv)
        args["scripts"] = util.locate_scripts_folder(argv)
        args["config_file"] = util.locate_config_file(argv)
        args["verbose"] = check_verbose(argv)

        # Time to create the directories
        if not skeleton_creator.create_skeleton(args):
            sys.exit(1)

        # Now, run the plugin (a.k.a plugins)
        run_plugins.run_plugins(args["verbose"])

    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
