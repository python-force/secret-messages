from encryption.monoalphabetic import Monoalphabetic


class Keycipher(Monoalphabetic):

    def cipher_string(self, keyword):
        super().cipher_string(keyword=keyword)
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

    def encrypt_decrypt(self, codeword, message, operation):
        codeword = codeword.upper()
        main_dict = self.cipher_string(codeword)
        phrase = message.upper().split()
        new_list = []
        for item in phrase:
            word = []
            for ch in item:
                for key, value in main_dict.items():
                    if operation == "encrypt":
                        if ch in value:
                            word.append(key)
                    else:
                        if ch in key:
                            word.append(value)
            word = "".join(word)
            new_list.append(word)
        return " ".join(new_list)

    def encrypt(self, message):
        codeword = input("Please specify the codeword, "
                         "all characters must be unique: ")
        return self.encrypt_decrypt(codeword, message, "encrypt")

    def decrypt(self, message):
        codeword = input("Please specify the codeword, "
                         "to decrypt the message: ")
        return self.encrypt_decrypt(codeword, message, "decrypt")
