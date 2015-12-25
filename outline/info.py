#!/usr/bin/python3

import version

def info():
    print("Outline v{0}\n".format(version.__version__))
    print("Copyright (c) Sean Francis N. Ballas. All rights reserved 2015.\n")

if __name__ == "__main__":
    info()
