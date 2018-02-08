
#!/usr/bin/env python3

import sys
import argparse
import string

def doStuff(filein,fileout,key,mode):
	fin_b = open(filein, mode='rb')  # binary read mode
	fout_b = open(fileout, mode='wb')  # binary write mode
	c    = fin_b.read()   
	

	key=int(key)
	fin_b.close()
	with open(filein, mode="rb") as fin_b:
		text=fin_b.read()
		if key in range(0,255):

			if mode.lower()=='e': #encrypt mode
				with open(fileout,mode='wb') as fout_b:

					for i in range(len(text)):
						fout_b.write(bytearray([(text[i]+key)%256]))
			elif mode.lower()=='d':decrypt mode
				with open(fileout,mode='wb') as fout_b:
					for i in range(len(text)):
						fout_b.write(bytearray([(text[i]-key)%256]))
			else:
				print ("Please enter a valid mode")

		else:
			print ("Please enter a valid key (between 0 and 255)")

def checkKey(key):
	if int(key) in range (0,255):
		proceed=True
	else:
		proceed=False
		print('Invalid key entered. Try again!')

if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k',dest='key',help='what key')
    parser.add_argument('-m',dest='mode',help='what mode')
    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key=args.key
    mode=args.mode
    doStuff(filein,fileout,key,mode)