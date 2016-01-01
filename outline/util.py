#!/usr/bin/python3

import sys

import info

def fragment_count_in_list(elem_list, elem):
    count = 0
    for list_elem in elem_list:
        if elem in list_elem:
            count += 1

    return count

def project_name_specified(elem_list):
    if not is_argument(elem_list[0]):
        return True

    return False

def locate_project_name(elem_list):
    if not is_argument(elem_list[0]):
        return elem_list[0]

    return False

def locate_config_file_in_args(elem_list):
    for list_elem in elem_list:
        if "-c" == list_elem:
            index = elem_list.index(list_elem) + 1
            if not "-" in elem_list[index] or not "--" in elem_list[index]:
                return elem_list[index]
        elif "--config" in list_elem:
            return list_elem[9:]

    return False

def check_verbose(elem_list):
    for list_elem in elem_list:
        if list_elem == "-v" or list_elem == "--verbose":
            return True

    return False

def arguments_valid(elem_list):
    for list_elem in elem_list:
        if list_elem[0] == "-" and not is_argument(list_elem):
            info.arg_error(list_elem)
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
