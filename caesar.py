import string

class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

class Caesar(Cipher):
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
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


"""
phrase = input("What phrase you would like me to process? ")

x = Caesar().encrypt(phrase)
x = x.split(" ")
x = ''.join(x)
x = x[:5] + " " + x[5:10] + " " + x[10:15] + " " + x[15:20] + " " + x[20:25] + " " + x[30:35] + " " + x[35:]

print (Fore.BLUE, "The phrase > " + phrase)
print (Fore.GREEN, "Was successfully sent to U-Boat 571 > " + x)
print (Fore.WHITE, "Have a wonderful day")
"""