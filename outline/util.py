#!/usr/bin/python3

import sys

import info

def fragment_count_in_list(elemList, elem):
    count = 0
    for listElem in elemList:
        if elem in listElem:
            count += 1

    return count

def project_name_count_in_list(elemList):
    count = 0
    for listElem in elemList:
        if not is_argument(listElem):
            count += 1

    return count

def locate_project_name(elemList):
    for listElem in elemList:
        if not is_argument(listElem):
            return listElem

    return False

def get_passed_arg_value(elemList, shortArg, longOpt):
    for listElem in elemList:
        if shortArg == listElem:
            index = elemList.index(listElem) + 1
            if not "-" in elemList[index] or not "--" in elemList[index]:
                return elemList[index]
        elif longOpt in listElem:
            optLen = len(longOpt)
            if len(listElem) > optLen:
                return listElem[optLen:]

    return False

def locate_scripts_folder(elemList):
    return get_passed_arg_value(elemList, "-s", "--scripts")

def locate_config_file(elemList):
    return get_passed_arg_value(elemList, "-c", "--config")

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
        arg == "-s" or
        arg == "-c" or
        arg == "--help" or
        arg == "--verbose" or
        arg == "--version" or
        "--scripts=" in arg or
        "--config=" in arg):
        return True

    return False
