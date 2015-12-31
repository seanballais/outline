#!/usr/bin/python3

import version

def info():
    print("Outline v{0}\n".format(version.__version__))
    print("Copyright (c) Sean Francis N. Ballais. All rights reserved 2015.\n")

def help():
    info()
    print("")
    print("Usage:\n")
    print("  outline <project_name> [-c <file> | --config=<file>] [-s <directory> | --scripts=<directory>] [-v | --verbose]\n")
    print("  outline -h | --help")
    print("  outline -V | --version")
    print("")
    print("Options:\n")
    print("  -h, --help                            Display the help text.\n")
    print("  -v, --verbose                         Output every operation.\n")
    print("  -V, --version                         Display the version and exit.\n")
    print("  -c <file>, --config=<file>            Specify the config file to be used.\n")
    print("                                        Otherwise, outline will choose the\n")
    print("                                        config file that will be used.\n")
    print("  -s <directory> --scripts=<directory>  Specify the directory where to look for\n")
    print("                                        third-party outline scripts.\n")

def arg_error(arg):
    print("outline: unknown argument: {0}\n".format(arg))
    print("Try 'outline --help' for more information.\n")

def display_config_error(config_file):
    print("Cannot find config file: {0}\n".format(config_file))
    print("Make sure you entered the right config file name.\n")

if __name__ == "__main__":
    info()
