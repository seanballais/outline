#!/usr/bin/python3

def elem_occurences_in_list(elemlist, elem):
    count = 0
    for listElem in elemList:
        if listElem == elem:
            count += 1

    return count

def elem_fragment_occurences_in_list(elemList, elem):
    count = 0
    for listElem in elemList:
        if elem in listElem:
            count += 1

    return count

def arguments_valid(elemList):
    for listElem in elemList:
        if listElem != "-h" or listElem != "--help" or
           listElem != "-v" or listElem != "--verbose" or
           listElem != "-V" or listElem != "--version" or
           listElem != "-s" or "--scripts" not in listElem or
           listElem != "-c" or "--config" not in listElem:
