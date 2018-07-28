from encryption.caesar import Cipher


class Monoalphabetic(Cipher):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = []
    for ch in alpha:
        alpha_list.append(ch)

    def check_message(self, message):
        """
        Validating a message if numbers being used in the message
        Monoalphabetic cipher
        :param message:
        :return:
        """
        if any(str.isdigit(x) for x in message):
            print("For this cipher numbers cannot be used, "
                  "this is monoalphabetic ciper.")
        else:
            return True

    def cipher_string(self, keyword=""):
        """
        Function used later in other classes
        :param message:
        :return:
        """
        pass
