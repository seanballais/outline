#!/usr/bin/python3

import info

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

if __name__ == "__main__":
    help()
