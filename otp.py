from caesar import Cipher
import string
import random

class Otp(Cipher):
    alphabet = string.ascii_uppercase
    alphabet_list = []
    for ch in alphabet:
        alphabet_list.append(ch)
    print(alphabet_list)
    main_dict = {
        "A": (0, 26), "B": (1, 27), "C": (2, 28), "D": (3, 29), "E": (4, 30), "F": (5, 31),
        "G": (6, 32), "H": (7, 33), "I": (8, 34), "J": (9, 35), "K": (10, 36), "L": (11, 37),
        "M": (12, 38), "N": (13, 39), "O": (14, 40), "P": (15, 41), "Q": (16, 42), "R": (17, 43),
        "S": (18, 44), "T": (19, 45), "U": (20, 46), "V": (21, 47), "W": (22, 48), "X": (23, 49),
        "Y": (24, 50), "Z": (25, 25)
    }

    def encrypt(self, message):
        message = message.upper().split()
        message = "".join(message)
        message_list = []
        for ch in message:
            message_list.append(self.main_dict[ch][0])

        print(message_list)

        # random key

        random_otp = [random.choice(self.alphabet_list) for _ in range(len(message))]
        print("".join(random_otp))
        for i, item in enumerate(random_otp):
            random_otp[i] = self.main_dict[item][0]

        print(random_otp)

        math_list = []
        for i, item in enumerate(message_list):
            try:
                result = message_list[i] + random_otp[i]
                math_list.append(result)
            except:
                print("The message or the otp has a different length")

        print(math_list)

        for i, item in enumerate(math_list):
            if item > 25:
                for key, value in self.main_dict.items():
                    if value[1] == item:
                        math_list[i] = key
            else:
                for key, value in self.main_dict.items():
                    if value[0] == item:
                        math_list[i] = key

        print(math_list)
        return "".join(math_list)


    def decrypt(self, message):
        message = message.upper().split()
        message = "".join(message)
        message_list=[]
        for ch in message:
            message_list.append(self.main_dict[ch][0])

        print(message_list)
        otp = input("What is otp?: ")
        otp = otp.upper()
        random_otp=[]
        for ch in otp:
            random_otp.append(self.main_dict[ch][0])
        print(random_otp)

        math_list = []
        for i, item in enumerate(message_list):
            if message_list[i] > random_otp[i]:
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
        print(math_list)
        return "".join(math_list)