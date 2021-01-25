#!/usr/bin/python
# coding=utf-8
# Originally Written By:Muhammad Hamza
# Source : Python2"
# Donot Recode It.
__author__ = "Muhammad Hamza"
__copyright = "Copyright (c) 2020-2025, Muhammad Hamza"


Description = """
This Tool Is Created To Hide Your Python Codes From The Eyes Of Copier.This Is Compatible With Python And Python2.7"""
import random,sys,logging

logging.basicConfig(level=logging.INFO)

def main(files,string):
	s=open(files).read()
	z=[]
	for i in s:
		z.append(ord(i))
	pea=[]
	for i in z:
		pea.append(string.replace("'","").replace('"','')*i)
	file="""
# coding=utf-8
# Encrypted By : Muhammad Hamza
# Github       : https://github.com/Hamzahash


hop_programmer={};exec("".join([chr(len(i)) for i in hop_programmer]))
	""".format(pea)
	open(files.replace(".py","en1.py"),"w").write(file)
	logging.info(" saved as "+files.replace(".py","en1.py"))

try:
	logging.info("Encryting Please Wait "+sys.argv[1]+" ...")
	main(sys.argv[1],sys.argv[2])
except:
	print("""

[!] ussage: plusobf.py <filename> 'string'
Example:
	python plusobf.py myscript.py '+'
""")



