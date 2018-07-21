from colorama import Fore, Back, Style
from caesar import Cipher, Caesar

encryption_dict = {1: "Caesar", 2: "Dude"}

def enc_list():
    for key, value in encryption_dict.items():
        print(str(key) + ": " + str(value))

def enc_selected():
    enc = input("Which encryption you would like to use? Please choose a number: ")
    for key, value in encryption_dict.items():
        if key == int(enc):
            print(value.capitalize() + " it is.")
            return key

def encrypt_the_phrase(phrase, i):
    if i == 1:
        x = Caesar().encrypt(phrase)
        x = x.split(" ")
        x = ''.join(x)
        x = x[:5] + " " + x[5:10] + " " + x[10:15] + " " + x[15:20] + " " + x[20:25] + " " + x[30:35] + " " + x[35:]

        print(Fore.BLUE, "The phrase > " + phrase)
        print(Fore.GREEN, "Was successfully sent to U-Boat 571 > " + x)
        print(Fore.WHITE, "Have a wonderful day")
    else:
        print("Duuuh")

def decrypt_the_phrase(phrase, i):
    if i == 1:
        x = Caesar().decrypt(phrase)
        print(Fore.BLUE, "The phrase > " + phrase)
        print(Fore.GREEN, "Was successfully sent to U-Boat 571 > " + x)
        print(Fore.WHITE, "Have a wonderful day")


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