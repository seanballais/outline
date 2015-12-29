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
        if listElem != "-h" or listElem != "--help" or
           listElem != "-v" or listElem != "--verbose" or
           listElem != "-V" or listElem != "--version" or
           listElem != "-s" or "--scripts=" not in listElem or
           listElem != "-c" or "--config=" not in listElem:
            count += 1

    return count

def locate_project_name(elemList):
    for listElem in elemList:
        if listElem != "-h" or listElem != "--help" or
           listElem != "-v" or listElem != "--verbose" or
           listElem != "-V" or listElem != "--version" or
           listElem != "-s" or "--scripts=" not in listElem or
           listElem != "-c" or "--config=" not in listElem:
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
        if "-" in listElem or "--" in listElem:
            if listElem != "-h" or listElem != "--help" or
               listElem != "-v" or listElem != "--verbose" or
               listElem != "-V" or listElem != "--version" or
               listElem != "-s" or "--scripts=" not in listElem or
               listElem != "-c" or "--config=" not in listElem:
                info.arg_error(listElem)
                return False

    return True
