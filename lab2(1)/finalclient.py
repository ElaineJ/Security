#Done by Elaine Cheong 1001721 and Sita Rajagopal 1001677

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote


# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r


def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    frequency={}
    characters=[]
    testsol=''
    challenge=str(challenge)
    challenge = challenge[:-2]
    mapper={}
    for c in challenge:  
         
        if c in frequency:
            frequency[c]+=1
        else:
            frequency[c]=1             
    message_order = sorted(frequency, key=lambda x: frequency[x], reverse=True) #sort the order of the ascii characters
    print(message_order)
    
    print(characters)
    print (frequency)
   
    #brute force is used 
    #list of all charcters is compared with the frequency analysis of sherlock text 
    mapper[' ']=message_order[0]
    mapper['e']=message_order[1]
    mapper['t']=message_order[2]
    mapper['a']=message_order[3]
    mapper['o']=message_order[4]
    mapper['h']=message_order[5]
    mapper['r']=message_order[6]
    mapper['n']=message_order[7]
    mapper['d']=message_order[8]
    mapper['i']=message_order[9]
    mapper['s']=message_order[10]
    mapper['l']=message_order[11]
    mapper['w']=message_order[12]
    mapper['\n']=message_order[13]
    mapper['g']=message_order[14]
    mapper[',']=message_order[15]
    mapper['u']=message_order[16]
    mapper['c']=message_order[17]
    mapper['m']=message_order[18]
    mapper['y']=message_order[19]
    mapper['f']=message_order[20]
    mapper['p']=message_order[21]
    mapper['.']=message_order[23]
    mapper['b']=message_order[24]
    mapper['k']=message_order[25]

    # this is done because the list that is sorted is always jumble up
    mapper['"']=message_order[message_order.index("J")]
    mapper['v']=message_order[message_order.index("N")]
    mapper['-']=message_order[28]
    mapper["'"]=message_order[message_order.index("0")]
    mapper['j']=message_order[message_order.index("-")]
    mapper['?']=message_order[message_order.index("<")]
    mapper['q']=message_order[message_order.index("B")]
    mapper['\t']=message_order[35]

    print(mapper)
    ans=''
    for c in challenge:
        for key in mapper:
            if mapper[key]==c:
                ans+=key
            
    solution = int(0).to_bytes(7408, 'big')
    conn.send(ans)
    message = conn.recvline()
    message = conn.recvline()
    print (ans)
    if b'Congratulations' in message:
        print(message)
    conn.close()
    


def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # some all zero mask.
    # TODO: find the magic mask! 
    mask=[0]*len(message)
    mask=bytearray(mask)

    mask[14]=1
    mask[15]=7
    mask[16]=2
    mask[17]=1

    #this is for the grade
    mask[24]=4

    message = XOR(challenge, mask)

    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'exact' in message:
        print(message)
    conn.close()


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = 'scy-phy.net'
    PORT = 1337

    sol1()
    sol2()
