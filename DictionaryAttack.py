'''
Created on Apr 29, 2021

@author: rayya
'''
# Hint1: how to produce hashes? Source: https://docs.python.org/2/library/hashlib.html#key-derivation
import hashlib, binascii #will use a built-in library called 'hashlib'
import time
import itertools

def hash(password, hashType):
    hashed_pwd = hashlib.pbkdf2_hmac(hashType, #later you will changes this to sha512
                         password.encode('utf-8'),# passowrd is encoded into binary  
                         'saltPhrase'.encode('utf-8'),# 'salt' is an extra bit of info added to the password. When using randomized 'salt' dictionary attacks becomes nealry impossible. For this project keep 'salt' static. In the real world 'salt' is randomized and later exctracted from the hashed password during the verififcation process. Essentially, the 'salt' portion of the hash can be separated from the password portion.
                         10) # number of iterations ('resolution') of the hashing computation)
    return binascii.hexlify(hashed_pwd)# converting binary to hex

dict_array=[]
dict_file = open("dict.txt","r") 

for line in dict_file:
    dict_array.append(line.rstrip('\n')) # rstrip('\n') removes newline characters from the words, you might not need this. 
    
password = input("Enter password:")
hashType = input("Do you want to hash with sha256 or sha512?")
print("Pwd is: "+password+" Length is: ",len(password))
print("Hash type is: " + hashType)

start = time.time()

hashed_pwd_hex=hash(password, hashType)
print(hashed_pwd_hex)

def findPassword(dictionary, words):
    guesses = 0
    for subset in itertools.permutations(dictionary, words):
        word = "".join(subset)
        if (len(word) == len(password)):
            guesses = guesses + 1
            if hash(word, hashType) == hashed_pwd_hex:
                return [word, guesses]

for L in range(1, 5):
    data = findPassword(dict_array, L)
    if data != None:
        finalTime = time.time()-start
        print("Guessed it! " + data[0])
        print("Elpased time: ", (finalTime), " seconds.")
        print("Guesses: ", data[1])
        break

