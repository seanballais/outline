#!/usr/bin/python3

import os

def run_plugins():
    # Loop through each directory to locate a scripts.oto file
    locations = {
        os.path.expanduser("~") + "/.outline/config/",
        "/usr/local/share/outline/",
        "/usr/share/outline/",
    }

    for loc in locations:
        try:
            script_order = open(loc + "script.oto", "r")
        except FileNotFoundError:
            script_order.close()
            continue

        line = script_order.readline()
        while line:
            line = line.strip()
            if line[0] == "#":
                continue

            re.sub("#.*", "", line)
            line = line.rstrip()

            
