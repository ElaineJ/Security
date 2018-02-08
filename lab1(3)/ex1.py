#!/usr/bin/env python3

# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Import libraries
import sys
import argparse
import string


def doStuff(filein,fileout,key,mode):
    # open file handles to both files
    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    fin_b = open(filein, mode='rb')  # binary read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')      # write mode
    fout_b = open(fileout, mode='wb')  # binary write mode
    c    = fin.read()         # read in file into c as a str
    # and write to fileout

    # close all file streams
    fin.close()
    fin_b.close()
    fout_b.close()

    # PROTIP: pythonic way
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        text = fin.read()
        # do stuff
        while checkKey(key):
            for c in text:
                if mode.lower()=='e' and c in string.printable:
                    charnum=string.printable.index(c)+int(key)
                    if charnum>len(string.printable):
                        charnum=charnum-len(string.printable)
                    newchar=string.printable[charnum]
                    #if newchar in string.printable:
                    fout.write(newchar)
                elif mode.lower()=='d' and c in string.printable:
                    charnum=string.printable.index(c)-int(key)
                    if charnum<0:
                        charnum=len(string.printable)+charnum
                    newchar=string.printable[charnum]
                    #if newchar in string.printable:
                    fout.write(newchar)
            break
        fout.close()





        #print (all(c in string.printable for c in text))
        # file will be closed automatically when interpreter reaches end of the block

def checkKey(key):
    if int(key) in range(1,len(string.printable)-1):
        proceed=True
    else:
        print("Invalid Key, Try Again")
        proceed=False
    return proceed



# our main function
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

    # all done


