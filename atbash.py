from caesar import Cipher
from monoalphabetic import Monoalphabetic

class Atbash(Monoalphabetic):

    def cipher_string(self):
        backwards_list = self.alpha_list[::-1]

        dict = {}
        for i in range(0, len(self.alpha_list)):
            dict[self.alpha_list[i]] = backwards_list[i]
        return (dict)

    def encrypt(self, message):
        main_dict = self.cipher_string()
        phrase = message.upper().split()
        new_list = []
        for item in phrase:
            word = []
            for ch in item:
                for key, value in main_dict.items():
                    if ch in value:
                        word.append(key)
            word = "".join(word)
            new_list.append(word)
        return " ".join(new_list)


    def decrypt(self, message):
        main_dict = self.cipher_string()
        phrase = message.upper().split()

        new_list = []
        for item in phrase:
            word = []
            for ch in item:
                for key, value in main_dict.items():
                    if ch in key:
                        word.append(value)
            word = "".join(word)
            new_list.append(word)
        return " ".join(new_list)