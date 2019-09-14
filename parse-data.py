#!/usr/bin/python
#
# Parse org-mode and store body text in dictionary
# organized by tags as class labels
#

from Orgnode import *

import sys
import os

from collections import defaultdict

filename = sys.argv[1]
nodelist = makelist(filename)

org = defaultdict(list)

# build tag dictionary with array of body text
for node in nodelist:
  if (len(node.Tags()) == 0):
    org["NOTAG"].append(node.Body())
  else:
    for tag in node.Tags():
       org[tag].append(node.Body())

# report doc count for each tag
for tag in org.keys():
   print("{}: {}".format(tag, len(org[tag])))
