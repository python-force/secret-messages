from colorama import Fore, Back, Style
from caesar import Caesar
from adfgvx import Adfgvx
from keywordcipher import Keycipher
from atbash import Atbash

encryption_dict = {1: "Caesar", 2: "Adfgvx", 3: "Keycipher", 4: "Atbash"}
phrase = ""
crypting_phrase = ""

def crypting_result(crypting_phrase):
    print(Fore.BLUE, "The phrase > " + phrase)
    print(Fore.GREEN, "Was successfully sent to U-Boat 571 > " + crypting_phrase)
    print(Fore.WHITE, "Have a wonderful day")

def enc_list():
    for key, value in encryption_dict.items():
        print(str(key) + ": " + str(value))

def enc_selected():
    enc = input("Which encryption you would like to use? Please choose a number: ")
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

def encrypt_the_phrase(phrase, i):
    cls = encryption(i)
    crypting_phrase = cls.encrypt(phrase)
    crypting_result(crypting_phrase)
    """
    crypting_phrase = crypting_phrase.split(" ")
    crypting_phrase = ''.join(crypting_phrase)
    crypting_phrase = crypting_phrase[:5] + " " + crypting_phrase[5:10] + " " + crypting_phrase[10:15] + " " + crypting_phrase[15:20] + " " + crypting_phrase[20:25] + " " + crypting_phrase[30:35] + " " + crypting_phrase[35:]
    """

def decrypt_the_phrase(phrase, i):
    cls = encryption(i)
    crypting_phrase = cls.decrypt(phrase)
    crypting_result(crypting_phrase)


while True:
    enc_list()
    i = enc_selected()
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

print ("Done Coding")