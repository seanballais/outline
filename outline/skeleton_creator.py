#!/usr/bin/python3

import os
import re

import info

def create_skeleton(args):
    # Search for the configuration file
    locations = {
        os.path.expanduser("~") + "/.outline/config/",
        "/usr/local/share/outline/config/",
        "/usr/share/outline/config/",
    }

    verbose = args["verbose"]

    config_file = locate_config_file(args["config_file"], locations)
    if not config_file:
        info.display_config_error(args["config_file"])
    else:
        if os.path.exists(os.getcwd() + "/" + args["project_name"]):
            print("Directory ('{0}') already exists.".format(args["project_name"]))
            return False
        else:
            # Create the project folder
            try:
                if verbose:
                    print("Creating folder: '{0}'...".format(args["project_name"]))

                os.makedirs(args["project_name"])
            except OSError:
                print("Cannot create folder: '{0}'. Make sure that you are permitted to create files in this directory.".format(args["project_name"]))
                return False

            # Create files and folders inside the project folder
            try:
                os.chdir(args["project_name"])
            except FileNotFoundError:
                print("Cannot enter directory: '{0}'.".format(args["project_name"]))
                return False

            if create_folders(config_file, verbose):
                print("Successfully created project ('{0}').".format(args["project_name"]))
            else:
                return False

    return True

def locate_config_file(config_file, locations):
    for loc in locations:
        if os.path.exists(loc):
            for currFile in os.listdir(loc):
                if currFile == config_file + ".otc":
                    return loc + currFile

    return False

def create_folders(config_file, verbose):
    try:
        dir_list = open(config_file, "r")
    except FileNotFoundError:
        if verbose:
            print("Configuration file ('{0}') does not exist.".format(config_list))

        return False

    line = dir_list.readline()
    while line:
        # Remove any comments from the line
        line = line.strip()
        if line[0] == "#":
            continue

        re.sub("#.*", "", line)
        line = line.rstrip()

        # Make the file or folder
        if line[len(line) - 1] != "/": # This one's a file
            try:
                if verbose:
                    print("Creating file: '{0}'...".format(line))

                project_file = open(line, "w+")
                project_file.close()
            except IOError:
                print("Cannot create file: '{0}'. Make sure that you are permitted to create files in this directory.".format(line))
                return False
        else: # This one's a directory
            try:
                if verbose:
                    print("Creating folder: '{0}'...".format(line))

                os.makedirs(line)
            except OSError:
                print("Cannot create directory: '{0}'. Make sure that you are permitted to create directories in this directory.".format(line))
                return False

        line = dir_list.readline()

    dir_list.close()

    return True
