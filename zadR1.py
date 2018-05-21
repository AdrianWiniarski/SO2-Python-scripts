#!/usr/bin/env python3
#
#Adrian Winiarski
#ZadP3
#pt tp 11:15
#

import subprocess

p=subprocess.Popen(["netstat","-tulpn"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

for line in p.stdout:
	data = line.split()
	cos = (data[3].decode('utf-8'))
	if ":" not in cos:
		continue
	print(cos)

