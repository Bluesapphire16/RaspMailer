"""Functions for configuration files."""

#################################################
#                                               #
# Copyright (c) 2018 the GreyCloud contributors #
# GNU GPL 3 license                             #
# (http://www.gnu.org/licenses/)                #
#                                               #
#################################################

import json

def getObjectFromJSON(file):
    "Gets an object from JSON file"""
    with open(file, "r") as f:
        return json.load(f)

def saveObjectInJSON(object, file):
    """Saves an object in JSON file"""
    with open(file, "w") as f:
        json.dump(object, f, indent=2)
