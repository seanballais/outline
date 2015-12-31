#!/usr/bin/python3

import version

def info():
    print("Outline v{0}".format(version.__version__))
    print("Copyright (c) Sean Francis N. Ballais. All rights reserved 2015.")

def help():
    info()
    print("")
    print("Usage:")
    print("  outline <project_name> [-c <file> | --config=<file>] [-v | --verbose]")
    print("  outline -h | --help")
    print("  outline -V | --version")
    print("")
    print("Options:")
    print("  -h, --help                            Display the help text.")
    print("  -v, --verbose                         Output every operation.")
    print("  -V, --version                         Display the version and exit.")
    print("  -c <file>, --config=<file>            Specify the config file to be used.")
    print("                                        Otherwise, outline will choose the")
    print("                                        config file that will be used.")

def arg_error(arg):
    print("outline: unknown argument: {0}".format(arg))
    print("Try 'outline --help' for more information.")

def display_config_error(config_file):
    print("Cannot find config file: {0}".format(config_file))
    print("Make sure you entered the right config file name.")

if __name__ == "__main__":
    info()
