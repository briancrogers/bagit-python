# Creates a valid bag using metadata values read from an ini file. The directory to bag (which may contain subdirectories)
# can either be passed as the first argument or entered when at the script prompt.
# Created by @RockefellerArchiveCenter for Project Electron
# Updated by Brian Rogers <b.c.rogers@swansea.ac.uk>

#!/usr/bin/env python

import bagit
import os
from datetime import datetime
import sys
import yaml


def make_bag(target, metadata):
    # make bag
    bag = bagit.make_bag(target, metadata)

def walkdict(d, metadata):
  for k,v in d.items():
     if isinstance(v, dict):
         walkdict(v, metadata)
     else:
         metadata[k] = v

def main():
    if len(sys.argv) == 3:
        # use target directory passed as argument
        target = sys.argv[1]

        with open(sys.argv[2], 'r') as file:
            bag_metadata = yaml.safe_load(file)

        metadata = {}
        walkdict(bag_metadata, metadata)
    else:
        print("Sorry, that does not seem to be a valid directory!")

    if os.path.isdir(target):
        make_bag(target, metadata)
    else:
        print("Sorry, that does not seem to be a valid directory!")

main()
