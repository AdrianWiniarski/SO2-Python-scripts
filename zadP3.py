#!/usr/bin/env python3
#
#Adrian Winiarski
#ZadP3
#pt tp 11:15
#

import sys
import os

soruce = sys.argv[1]
dest = sys.argv[2]

file1 = os.listdir(soruce)
file2 = os.listdir(dest)

for filename in file1:
	if not os.path.isfile(os.path.join(dest, filename)):
		os.rename(os.path.join(soruce, filename), os.path.join(dest, filename))
