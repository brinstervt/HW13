
# Hint1: how to produce hashes? Source: https://docs.python.org/2/library/hashlib.html#key-derivation
import hashlib, binascii #will use a built-in library called 'hashlib'
import time
import itertools

def hash(password):
    hashed_pwd = hashlib.pbkdf2_hmac('sha256', #later you will changes this to sha512
                         password.encode('utf-8'),# passowrd is encoded into binary  
                         'saltPhrase'.encode('utf-8'),# 'salt' is an extra bit of info added to the password. When using randomized 'salt' dictionary attacks becomes nealry impossible. For this project keep 'salt' static. In the real world 'salt' is randomized and later exctracted from the hashed password during the verififcation process. Essentially, the 'salt' portion of the hash can be separated from the password portion.
                         10) # number of iterations ('resolution') of the hashing computation)
    return binascii.hexlify(hashed_pwd)# converting binary to hex

dict_array=[]
dict_file = open("dict.txt","r") 

for line in dict_file:
    dict_array.append(line.rstrip('\n')) # rstrip('\n') removes newline characters from the words, you might not need this. 
    
password = input("Enter password:")
print("Pwd is:"+password+" Length is: ",len(password))

start = time.time()

hashed_pwd_hex=hash(password)
print(hashed_pwd_hex)

# for L in range(0, 5):
#     for subset in itertools.permutations(dict_array, L):
#         word = "".join(subset)
#         if (len(word) == len(password)):
#             if hash(word) == hashed_pwd_hex:
#                 print("Guessed it! " + word)
#                 print("Elpased time: ", (time.time()-start), " seconds.")
#                 break
#     break

def findPassword(dictionary, words):
    for subset in itertools.permutations(dictionary, words):
        word = "".join(subset)
        if (len(word) == len(password)):
            if hash(word) == hashed_pwd_hex:
                print("Guessed it! " + word)
                print("Elpased time: ", (time.time()-start), " seconds.")
                return word
            
for L in range(1, 5):
    word = findPassword(dict_array, L)
    if word != None:
        break

#Hint4: iterating over the word list comparing the hashes 
#for word in combination:
#    if hash(word) == hashed_pwd_hex:
#        print("Guessed it! " + word)
#        break;
#    else:
#        print("Wrong:"+word)
        
        

#Hint5: measuring time difference.