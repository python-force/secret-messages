from encryption.monoalphabetic import Monoalphabetic


class Atbash(Monoalphabetic):

    def cipher_string(self):
        """
        Flipping alphabet list and creating dictionary
        with corresponding keys and values
        :return:
        """
        backwards_list = self.alpha_list[::-1]

        dict = {}
        for i in range(0, len(self.alpha_list)):
            dict[self.alpha_list[i]] = backwards_list[i]
        return (dict)

    def encrypt_decrypt(self, message):
        """
        Atbash encrypt/decrypt algorithm
        Encrypting and Decrypting based on flipped alphabet dictionary
        Full Algorithm here: https://en.wikipedia.org/wiki/Atbash
        :param message:
        :return:
        """
        if self.check_message(message):
            phrase = message.upper().split()
            main_dict = self.cipher_string()
            new_list = []
            for item in phrase:
                word = []
                for ch in item:
                    for key, value in main_dict.items():
                        if ch in value:
                            word.append(key)
                word = "".join(word)
                new_list.append(word)
            return new_list

    def encrypt(self, message):
        """
        Encrypt the message
        :param message:
        :return:
        """
        return " ".join(self.encrypt_decrypt(message))

    def decrypt(self, message):
        """
        Decrypt the message
        :param message:
        :return:
        """
        return " ".join(self.encrypt_decrypt(message))
