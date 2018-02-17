#Name: Sita Rajagopal (1001677) and Elaine Cheong Yu Shan (1001721)

import hashlib

from itertools import permutations
from itertools import combinations 
import time


fin=open('dictionary1.txt',mode='r')
words=fin.read()
wordlines=words.splitlines()
fin_hash=open("hashes.txt",mode='r')
hashwords=fin_hash.read()
hashlines=hashwords.splitlines()  
fout=open('resultst.csv',mode='w')

hashlines.remove("")
hashlines.remove("Strong:")
hashlines.remove("Weak:")
hashlines.remove("Moderate:") 

hashlines=filter(None,hashlines)
newhash=[]
for h in hashlines:
    newhash.append(h[h.index('.')+2:])  
wordlines = list(set(wordlines))
for word in wordlines:
    hashpos=hashlib.md5(str.encode(word)).hexdigest()
    if hashpos in newhash:
        print(hashpos,word)
        ans=hashpos+', '+word+'\n'
        fout.write(ans)
    
    




   


    
   


