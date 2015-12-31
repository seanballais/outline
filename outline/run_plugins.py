#!/usr/bin/python3

import os
import importlib.machinery

def run_plugins(verbose):
    # Loop through each directory to locate a scripts.oto file
    locations = {
        os.path.expanduser("~") + "/.outline/scripts/",
        "/usr/local/share/outline/scripts/",
        "/usr/share/outline/scripts/",
    }

    for loc in locations:
        try:
            script_order = open(loc + "script.oto", "r")
        except FileNotFoundError:
            if verbose:
                print("script.oto not located in directory ('{0}'). Moving on...".format(loc))
            continue

        line = script_order.readline()
        while line:
            # Remove any comments from the line
            line = line.strip()
            if line[0] == "#":
                continue

            re.sub("#.*", "", line)
            line = line.rstrip()

            # Check if the plugin exists and if so, run it
            plugin = loc + line
            if os.path.exists(plugin):
                if verbose:
                    print("Running plugin: {0}...".format(line))

                loader = importlib.machinery.SourceFileLoader("outline_plugin", plugin)
                module = loader.load_module()
                module.main()
            else:
                if verbose:
                    print("Plugin ('{0}') doesn't exist.".format(line))

                continue

            line = script_order.readline()

        script_order.close()

    return True
