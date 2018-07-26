from caesar import Cipher
from monoalphabetic import Monoalphabetic

class Keycipher(Monoalphabetic):

    def cipher_string(self, keyword):
        keyword_list = []
        for ch in keyword:
            keyword_list.append(ch)

        beta_list = self.alpha_list.copy()
        for ch in keyword_list:
            if ch in beta_list:
                beta_list.remove(ch)

        cipher_list = keyword_list + beta_list
        dict = {}
        for i in range(0, len(cipher_list)):
            dict[self.alpha_list[i]] = cipher_list[i]
        return (dict)

    def encrypt(self, message):
        main_dict = self.cipher_string("PREDATO")
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
        main_dict = self.cipher_string("PREDATO")
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