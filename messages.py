import os
# from colorama import Fore, Back, Style
from encryption.caesar import Caesar
from encryption.adfgvx import Adfgvx
from encryption.keywordcipher import Keycipher
from encryption.atbash import Atbash
from encryption.otp import Otp

encryption_dict = {1: "Caesar", 2: "Adfgvx", 3: "Keycipher", 4: "Atbash"}
phrase = ""
crypting_phrase = ""


def otp_encryption(crypting_phrase):
    """
    OTP - Encrypting already encrypted message with One Time Pad
    :param crypting_phrase:
    :return:
    """
    otp_encrypted = Otp().encrypt(crypting_phrase)
    return otp_encrypted


def otp_decrypt(phrase):
    """
    Decrypting the message with One Time Pad
    :param phrase:
    :return:
    """
    otp_decrypted = Otp().decrypt(phrase)
    return otp_decrypted


def crypting_result(crypting_phrase):
    """
    Final encrypted message being displayed on the screen
    :param crypting_phrase:
    :return:
    """
    print("The phrase > " + phrase)
    print("Was successfully sent to U-Boat 571 > " + crypting_phrase)
    print("Have a wonderful day")


def enc_list():
    """
    Displaying available encryption methods
    :return:
    """
    for key, value in encryption_dict.items():
        print(str(key) + ": " + str(value))


def check_encryption(enc):
    """
    Validation of the user's choice of the encryption
    :param enc:
    :return:
    """
    try:
        int(enc)
        return True
    except:
        print("Wrong Selection")
        return False


def enc_selected():
    """
    Encryption method selection
    :return:
    """
    enc = input("Which encryption you would like to use? "
                "Please choose a number: ")
    if check_encryption(enc):
        for key, value in encryption_dict.items():
            if key == int(enc):
                print(value.capitalize() + " it is.")
                return key


def encryption(i):
    """
    Based on the encrytption method selected - the Class will be selected
    :param i:
    :return:
    """
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


def check_phrase(crypting_phrase, encryption):
    """
    1. If the encrypted message is None, message was not typed/provided based on rules
    2. If the encrypted message was created, check with user if to use OTP
    3. If the method is decrypt, simply decrypt the message
    :param crypting_phrase:
    :param encryption:
    :return:
    """
    if crypting_phrase is None:
        crypting_phrase = "Cipher is unable to be processed. " \
                          "Please check your message."
        crypting_result(crypting_phrase)
    else:
        if encryption == "encrypt":
            otp_selection = input("Would you like to use OTP? y/n")
            if otp_selection == "y":
                result = otp_encryption(crypting_phrase)
                crypting_result(result)
            else:
                crypting_result(crypting_phrase)
        else:
            crypting_result(crypting_phrase)


def encrypt_the_phrase(phrase, i):
    """
    Encrypt the message based on selected encryption Class
    :param phrase:
    :param i:
    :return:
    """
    cls = encryption(i)
    crypting_phrase = cls.encrypt(phrase)
    check_phrase(crypting_phrase, "encrypt")


def decrypt_the_phrase(phrase, i):
    """
    Decrypt the message bases on the selected Class
    :param phrase:
    :param i:
    :return:
    """
    cls = encryption(i)
    crypting_phrase = cls.decrypt(phrase)
    check_phrase(crypting_phrase, "decrypt")


def clear_screen():
    if os.system == "nt":
        os.system('cls')
    else:
        os.system('clear')

# Script doesn't execute when imported
if __name__ == '__main__':
    # The script will keep running till the user is satisfied
    while True:
        # show the list of the encryption methods
        enc_list()

        # selected encryption
        i = enc_selected()

        # validation if the input is a number (int)
        if isinstance(i, int):

            # Specify the message you would like to encrypt
            phrase = input("What phrase you would like me to process? ")

            # User will be asked to choose to encrypt/decrypt the message
            print("1.encrypt")
            print("2.decrypt")
            type = input("Are we encrypting or decrypting? "
                         "Please choose from the following: ")

            # Based on the selection encryption will happen
            # or decrytpion with OTP decrytpion first, if it was chosen while
            # encryption process
            if int(type) == 1:
                encrypt_the_phrase(phrase, i)
            else:
                otp_decrypt_selection = input("Have you used to OPT to encrypt the message? y/n ")
                if otp_decrypt_selection == "n":
                    decrypt_the_phrase(phrase, i)
                else:
                    if otp_decrypt(phrase) is not None:
                        decrypt_the_phrase(otp_decrypt(phrase), i)
                    else:
                        crypting_phrase = "Cipher is unable to be processed. " \
                                          "Please check your message."
                        crypting_result(crypting_phrase)

            # Ask user if to continue with more messages
            ask = input("Continue? y/n ")
            if ask == "n":
                break
            else:
                clear_screen()
        else:
            # Validation if selection is not a number clear the screen
            # and ask again
            clear_screen()
            print("Please check your selection.")

    print("Done Coding")
