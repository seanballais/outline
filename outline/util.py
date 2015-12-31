#!/usr/bin/python3

import sys

import info

def fragment_count_in_list(elemList, elem):
    count = 0
    for listElem in elemList:
        if elem in listElem:
            count += 1

    return count

def project_name_specified(elemList):
    if not is_argument(elemList[0]):
        return True

    return False

def locate_project_name(elemList):
    if not is_argument(elemList[0]):
        return elemList[0]

    return False

def locate_config_file(elemList):
    for listElem in elemList:
        if "-c" == listElem:
            index = elemList.index(listElem) + 1
            if not "-" in elemList[index] or not "--" in elemList[index]:
                return elemList[index]
        elif "--config" in listElem:
            optLen = len(longOpt)
            if len(listElem) > optLen:
                return listElem[optLen:]

    return False

def check_verbose(elemList):
    for listElem in elemList:
        if listElem == "-v" or listElem == "--verbose":
            return True

    return False

def arguments_valid(elemList):
    for listElem in elemList:
        if listElem[0] == "-" and not is_argument(listElem):
            info.arg_error(listElem)
            return False

    return True

def is_argument(arg):
    if (arg == "-h" or
        arg == "-v" or
        arg == "-V" or
        arg == "-c" or
        arg == "--help" or
        arg == "--verbose" or
        arg == "--version" or
        "--config=" in arg):
        return True

    return False
