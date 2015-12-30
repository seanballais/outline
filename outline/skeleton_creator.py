#!/usr/bin/python3

import os

import info

def create_skeleton(args, configName):
    # Search for the configuration file
    locations = {
        os.path.expanduser("~") + "/.outline/config/",
        "/usr/local/share/outline/",
        "/usr/share/outline/",
    }

    # Search through each directory for the configuration file
    config_file = locate_config_file(locations)
    if not config:
        info.display_config_error(args["config_file"])
    else:


def locate_config_file(locations):
    for loc in locations:
        if os.path.exists(loc):
            for currFile in os.listdir(loc):
                if currFile == args["config_file"] + ".otc":
                    return os.path.abspath(currFile)

    return False

def create_folders(config_file):
    dir_list = open(config_file, "r")
    line = dir_list.readline()
    while line:
        line = line.strip()
        if line[0] == "#": # The line is a comment
            continue
        else: # Oh! Oh! This one's probably a directory now.
