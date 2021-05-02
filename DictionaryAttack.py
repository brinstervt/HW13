'''
Created on Apr 29, 2021

@author: rayya
'''
# Hint1: how to produce hashes? Source: https://docs.python.org/2/library/hashlib.html#key-derivation
import hashlib, binascii  # will use a built-in library called 'hashlib'
import time
import itertools
import matplotlib.pyplot as plt
import numpy as np


# Hashes the the word given using the hashtype given which can be sha256 or sha512
def hash(password, hashType):
    hashed_pwd = hashlib.pbkdf2_hmac(hashType,  # later you will changes this to sha512
                         password.encode('utf-8'),  # passowrd is encoded into binary  
                         'saltPhrase'.encode('utf-8'),  # 'salt' is an extra bit of info added to the password. When using randomized 'salt' dictionary attacks becomes nealry impossible. For this project keep 'salt' static. In the real world 'salt' is randomized and later exctracted from the hashed password during the verififcation process. Essentially, the 'salt' portion of the hash can be separated from the password portion.
                         100)  # number of iterations ('resolution') of the hashing computation)
    return binascii.hexlify(hashed_pwd)  # converting binary to hex


# Searches through the list of words in the dictionary and finds the password.
# It first creates the permutations and then it will see if the word permutations
# match the length of the password. If it has the same length, then it will hash it
# and see if it is the same as the hashed password.
def findPassword(dictionary, words):
    guesses = 0
    for subset in itertools.permutations(dictionary, words):
        word = "".join(subset)
        if (len(word) == len(password)):
            guesses = guesses + 1
            if hash(word, hashType) == hashed_pwd_hex:
                return [word, guesses]

# Creates a list to store the words in the dictionary
dict_array = []
dict_file = open("dict.txt", "r") 
for line in dict_file:
    dict_array.append(line.rstrip('\n'))  # rstrip('\n') removes newline characters from the words, you might not need this. 

# The type of hashes that all of the passwords you input would be
hashType = input("Do you want to hash with sha256 or sha512? ")

# Store the lengths of the password and the time it takes for the passwords to be guessed.
x = []
y = []

# Guesses need to find all the passwords given.
totalGuesses = 0

# Asks the user how many words they will be searching for so that they can all be plotted.
totalWords = input("How many words would you passwords would you like to input in total? ")

# Finds the length of the smallest word in the dictionary to determine the maximum number of words
# in the permutations that will be made to find the password.
minLength = len(dict_array[0])
for word in dict_array:
    if (len(word) < minLength):
        minLength = len(word)
        
# Finds the password using the length of the password and the hashed version of the password.
for z in range(0, int(totalWords)):
    # Asks user for the password.
    password = input("Enter password: ")
    print("Pwd is: " + password + " Length is: ", len(password))
    print("Hash type is: " + hashType)
    
    # Starts a timer to determine the time it takes to find the password.
    start = time.time()

    # Hashes the password.
    hashed_pwd_hex = hash(password, hashType)
    print(hashed_pwd_hex)

    # Finds the password, prints out the results, and adds it to the lists for plotting.
    # Range for the for loops is made to find the maximum amount of words that can be
    # in the password from the dictionary using the length of the smallest word.
    for L in range(1, len(password) // minLength + (len(password) % minLength > 0)):
        data = findPassword(dict_array, L)
        if data != None:
            finalTime = time.time() - start
            finalGuesses = data[1] 
            x.append(finalTime)
            y.append(len(password))
            totalGuesses = totalGuesses + finalGuesses
            print("Guessed it! " + data[0])
            print("Elpased time: ", (finalTime), " seconds.")
            print("Guesses: ", finalGuesses)
            break
       
# set x, y, slope
m, b = np.polyfit(x, y, 1)

# labels
plt.ylabel('Password Length', fontsize=9)
plt.xlabel('Time to Guess Password (sec)', fontsize=9)
plt.title('Hash Type: ' + hashType + '\n Dictionary Size: ' + str(len(dict_array)) + '\n Time Required to Guess: ' + str(sum(x)) + ' sec\n Number of Guesses: ' + str(totalGuesses), fontsize=8)
plt.plot(x, y, 'o')

# plot slope
axes = plt.gca()
x_vals = np.array(axes.get_xlim())
y_vals = b + m * x_vals
plt.plot(x_vals, y_vals, '-')
plt.show()