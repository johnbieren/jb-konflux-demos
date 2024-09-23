#!/usr/bin/env python3

import argparse
import json
import os
import shlex

parser = argparse.ArgumentParser()
parser.add_argument(
    "--test-arg",
    required=True,
)
args = parser.parse_args()
 
# Data to be written
dictionary = {
    "name": "jira",
    "example-argument": args.test_arg,
    "issues": [
        "RELEASE-1",
        "RELEASE-2"
    ]
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
#with open("collector-1.json", "w") as outfile:
#    outfile.write(json_object)
os.system("echo " + shlex.quote(json_object))
