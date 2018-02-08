#Done by: Elaine Cheong 1001721 & Sita Rajagopal 1001677


import sys
import argparse
import string
import subprocess




def doStuff(filein,fileout):
	fin_b = open(filein, mode='rb')  # binary read mode
	fout_b = open(fileout, mode='wb')  # binary write mode
	c    = fin_b.read()   
	#key=int(key)
	fin_b.close()
	with open(filein, mode="rb") as fin_b:
		text=fin_b.read()
		for key in range (0,255):
			with open((fileout.rsplit(".",1)[0]) + str(key)+".png",mode='wb') as fout_b: #save all values of k as an png file
				fout_b.write(bytearray([(text[i]-key)%256 for i in range(len(text))]))
			fout_b.close()
			result=subprocess.run(['file',fileout.rsplit(".",1)[0] + str(key)+".png"],stdout=subprocess.PIPE) #finding the correct file that has PNG data image
			if "PNG" in str(result.stdout):
				print(result.stdout)



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


    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    doStuff(filein,fileout)