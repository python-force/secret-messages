from encryption.monoalphabetic import Monoalphabetic


class Keycipher(Monoalphabetic):

    def cipher_string(self, keyword):
        """
        Inheritance of Monoalphabetic Class
        Removing characters from alphabet and adding the keyword characters to 1st place
        Creating dictionary
        Full Algorithm here: https://en.wikipedia.org/wiki/Keyword_cipher
        :param keyword:
        :return:
        """
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
        """
        Encryption / Decrytpion of a message based on the main dictionary
        Full Algorithm here: https://en.wikipedia.org/wiki/Keyword_cipher
        :param codeword:
        :param message:
        :param operation:
        :return:
        """
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
        """
        Encryption - Specify keyword - all characters must be unique
        :param message:
        :return:
        """
        codeword = input("Please specify the codeword, "
                         "all characters must be unique: ")
        for ch in codeword:
            occurences = codeword.count(ch)
            if occurences > 1:
                print("You have chosen a word without unique characters.")
                return None
            else:
                return self.encrypt_decrypt(codeword, message, "encrypt")

    def decrypt(self, message):
        """
        Decryption - Specify keyword - all characters must be unique
        :param message:
        :return:
        """
        codeword = input("Please specify the codeword, "
                         "to decrypt the message: ")
        for ch in codeword:
            occurences = codeword.count(ch)
            if occurences > 1:
                print("Your codeword is wrong.")
                return None
            else:
                return self.encrypt_decrypt(codeword, message, "decrypt")
        return self.encrypt_decrypt(codeword, message, "decrypt")
