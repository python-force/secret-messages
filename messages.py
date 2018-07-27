import os
# from colorama import Fore, Back, Style
from caesar import Caesar
from adfgvx import Adfgvx
from keywordcipher import Keycipher
from atbash import Atbash

encryption_dict = {1: "Caesar", 2: "Adfgvx", 3: "Keycipher", 4: "Atbash"}
phrase = ""
crypting_phrase = ""

def crypting_result(crypting_phrase):
    print("The phrase > " + phrase)
    print("Was successfully sent to U-Boat 571 > " + crypting_phrase)
    print("Have a wonderful day")

def enc_list():
    for key, value in encryption_dict.items():
        print(str(key) + ": " + str(value))

def check_encryption(enc):
    try:
        int(enc)
        return True
    except:
        print("Wrong Selection")
        return False

def enc_selected():
    enc = input("Which encryption you would like to use? Please choose a number: ")
    if check_encryption(enc):
        for key, value in encryption_dict.items():
            if key == int(enc):
                print(value.capitalize() + " it is.")
                return key

def encryption(i):
    cls = ""
    if i == 1:
        cls = Caesar()
    elif i == 2:
        cls = Adfgvx()
    elif i == 3:
        cls = Keycipher()
    elif i == 4:
        cls = Atbash()
    return cls

def check_phrase(crypting_phrase):
    if crypting_phrase == None:
        crypting_phrase = "Cipher is unable to be processed. Please check your message."
        crypting_result(crypting_phrase)
    else:
        crypting_result(crypting_phrase)

def encrypt_the_phrase(phrase, i):
    cls = encryption(i)
    crypting_phrase = cls.encrypt(phrase)
    
    check_phrase(crypting_phrase)

def decrypt_the_phrase(phrase, i):
    cls = encryption(i)
    crypting_phrase = cls.decrypt(phrase)
    check_phrase(crypting_phrase)


while True:
    enc_list()
    i = enc_selected()
    if isinstance(i, int):
        phrase = input("What phrase you would like me to process? ")
        print("1.encrypt")
        print("2.decrypt")
        type = input("Are we encrypting or decrypting? Please choose from the following: ")
        if int(type) == 1:
            encrypt_the_phrase(phrase, i)
        else:
            decrypt_the_phrase(phrase, i)

        ask = input("Continue? y/n ")
        if ask == "n":
            break
    else:
        if os.system == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print("Please check your selection.")

print ("Done Coding")