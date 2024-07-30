'''
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.

string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.

string.digits
The string '0123456789'.

string.hexdigits
The string '0123456789abcdefABCDEF'.

string.octdigits
The string '01234567'.

string.punctuation
String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.

string.printable
String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.

string.whitespace
A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
'''

import string

import random

import sys

if __name__ == "__main__":#check if the current script is being run directly by the Python interpreter
    set1 = string.ascii_lowercase
    #print(set1)
    set2 = string.ascii_uppercase
    #print(set2)
    set3 = string.digits
    #print(set3)
    set4 = string.punctuation
    #print(set4)
    
    # Filter out gibberish characters-- Gibberish characters" typically refer to random or nonsensical characters that do not serve any meaningful purpose in a given contex
     
    try:
        password_length = int(input("Enter the length of the password required for you..?:\n")) #will take input in next line, 
    except:
        sys.exit("Invalid Length type")
        
    set = []
    set.extend(list(set1)) # yek paxi arko thapdai janxa
    set.extend(list(set2))
    set.extend(list(set3))
    set.extend(list(set4))
    #print(set)
    
    random.shuffle(set) #mix-max garxa value sablai
    #print(set)
    
    
     
    print("Your password is:")
    print("".join(set[0:password_length]))
    
    
    ''' comment out the random.shuffle(set) and directly you can
        print("".join(random.sample(set, password_length))) 
    '''