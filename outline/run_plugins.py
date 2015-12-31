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
            script_order.close()

            if verbose:
                print("scirpt.oto not located in directory ('{0}'). Moving on...\n".format(loc))
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
                    print("Running plugin: {0}...\n".format(line))

                loader = importlib.machinery.SourceFileLoader("outline_plugin", plugin)
                module = loader.load_module()
                module.main()
            else:
                if verbose:
                    print("Plugin ('{0}') doesn't exist.\n".format(line))

                continue

            line = script_order.readline()

    return True
