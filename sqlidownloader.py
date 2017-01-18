#! /usr/bin/python

import os
import sys


sqlmap_arg = sys.argv[1]
dirw = sys.argv[2]
files = sys.argv[3].split()

def download_file(f):
	ret = os.system("sqlmap " + sqlmap_arg  + " --batch")
	print ret


while (files):
	download_file(files.pop())

print "descarga finalizada en " + dirw

