from encryption.cipher import Cipher
import string

class Caesar(Cipher):
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        """
        3x alphabet
        Forward: Moving in alphabet in 3 positions forward
        Backward: Moving in alphabet in 3 positions back
        :param offset:
        """
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        """
        Encryption method creating a string of characters shifted forward
        Full Algorithm here: https://en.wikipedia.org/wiki/Caesar_cipher
        :param text:
        :return:
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        """
        Decrypting method creating a string of characters shifted backward
        Full Algorithm here: https://en.wikipedia.org/wiki/Caesar_cipher
        :param text:
        :return:
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
