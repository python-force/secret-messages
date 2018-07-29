from encryption.cipher import Cipher
import string
import random


class Otp(Cipher):
    alphabet = string.ascii_uppercase
    alphabet_list = []
    for ch in alphabet:
        alphabet_list.append(ch)

    main_dict = {
        "A": (0, 27), "B": (1, 28), "C": (2, 29),
        "D": (3, 30), "E": (4, 31), "F": (5, 32),
        "G": (6, 33), "H": (7, 34), "I": (8, 35),
        "J": (9, 36), "K": (10, 37), "L": (11, 38),
        "M": (12, 39), "N": (13, 40), "O": (14, 41),
        "P": (15, 42), "Q": (16, 43), "R": (17, 44),
        "S": (18, 45), "T": (19, 46), "U": (20, 47),
        "V": (21, 48), "W": (22, 49), "X": (23, 50),
        "Y": (24, 51), "Z": (25, 52), " ": (26, 26)
    }

    random_ch = ["!", "@", "#", "$", "%", "^", "&",
                 "*", "(", ")", "{", "}", "]", "[", "?"]

    def salt_with_random(self, math_list):
        """
        Pick random characters and salt the message to know where the spaces are for proper encryption
        :param math_list:
        :return:
        """
        for i, item in enumerate(math_list):
            if item == " ":
                math_list[i] = random.choice(self.random_ch)
        math_list = "".join(math_list)

        block_list = []
        for i in range(0, len(math_list), 5):
            block_list.append(math_list[i:i + 5])

        return block_list

    def desalt_random(self, message):
        """
        Remove random characters to unlock the message for decryption
        :param math_list:
        :return:
        """
        message_char = []
        for ch in message:
            message_char.append(ch)
        for i, item in enumerate(message_char):
            if item in self.random_ch:
                message_char[i] = " "
        return message_char

    def encrypt(self, message):
        """
        One Time Pad Encryption
        Generate a random key and encrypt the message with it with mod 27 (using " " as extra character)
        Full Algorithm Source: http://users.telenet.be/d.rijmenants/en/onetimepad.htm
        :param message:
        :return:
        """
        # message = message.upper().split()
        # message = "".join(message)
        message = message.upper()
        message_list = []
        for ch in message:
            message_list.append(self.main_dict[ch][0])

        # Generate a random key
        random_otp = [random.choice(self.alphabet_list) for _ in range(len(message))]
        print("Your OTP is: " + str("".join(random_otp)))
        print("Use the OTP to unlock the message.")

        # Convert Random key to integers
        for i, item in enumerate(random_otp):
            random_otp[i] = self.main_dict[item][0]

        # Do the math with Random Key and the message
        math_list = []
        for i, item in enumerate(message_list):
            try:
                result = message_list[i] + random_otp[i]
                math_list.append(result)
            except:
                print("The message and OTP does not have the same length")
                continue

        # Logic to do mod27
        for i, item in enumerate(math_list):
            for key, value in self.main_dict.items():
                if item > 26:
                    if value[1] == item:
                        math_list[i] = key
                else:
                    if value[0] == item:
                        math_list[i] = key

        # Algorithm for 5 block characters
        padding = input("Would you like to use block 5 characters? y/n ")
        if padding == "y":
            math_list = self.salt_with_random(math_list)
            return " ".join(math_list)
        else:
            math_list = "".join(math_list)
            return math_list

    def decrypt(self, message):
        """
        One Time Pad Decryption
        Removing random characters to desalt the message
        Logic to decrypt the message with OTP
        Decrypt by mod27
        Full Algorithm Source: http://users.telenet.be/d.rijmenants/en/onetimepad.htm
        :param message:
        :return:
        """
        # message = message.upper().split()
        # message = "".join(message)
        # desalting the message to remove 5 characters blocks
        padding = input("Have you used 5 characters blocks? y/n ")
        if padding == "y":
            message = message.replace(" ", "")
            message = self.desalt_random(message)
            message = "".join(message)

        message = message.upper()
        message_list = []
        for ch in message:
            message_list.append(self.main_dict[ch][0])

        # OTP Encryption / process the message with OTP
        otp = input("What is the OTP that was generated for you during "
                    "encryption process?: ")
        otp = otp.upper()
        random_otp = []
        for ch in otp:
            random_otp.append(self.main_dict[ch][0])

        # If OTP is correct, decrypt the message with mod27
        if len(message_list) != len(random_otp):
            print("You typed a wrong OTP.")
            return None
        else:
            math_list = []
            for i, item in enumerate(message_list):
                if message_list[i] >= random_otp[i]:
                    x = message_list[i] - random_otp[i]
                    for key, value in self.main_dict.items():
                        if value[0] == x:
                            math_list.append(key)
                else:
                    for key, value in self.main_dict.items():
                        if item == value[0]:
                            x = value[1] - random_otp[i]
                            for key, value in self.main_dict.items():
                                if value[0] == x:
                                    math_list.append(key)
            return "".join(math_list)
