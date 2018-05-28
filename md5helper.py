# Copyright (c) 2018 Ilker Oztelcan
# See LICENSE file for details.

import hashlib
import sys
import os.path

INTROTEXT ="\
##############################################\n\
############# Windows MD5 Helper #############\n\
Because development on Windows is a nightmare!\n\
##############################################\n"

HELPTEXT ="\
This small script exists to provide quick md5sum calculation on Windows.\n\n\
Usage:\n\
1. Shift right-click on the file of which md5sum will be calculated.\n\
2. Click on *Copy as path*.\n\
3. Paste the copied path as the input argument.\n\n\
Have fun.\n"

print INTROTEXT

if len(sys.argv) < 2:
	print "Add -h for help on how to use."
	exit(1)
if (sys.argv[1] == "-h"):
	print HELPTEXT
	exit(0)

file_path = os.path.abspath(sys.argv[1])
md5sum = hashlib.md5()

with open(file_path, "rb") as f:
	for chunk in iter(lambda: f.read(4096), ""):
		md5sum.update(chunk)
		
print md5sum.hexdigest()

		

	