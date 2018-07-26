from caesar import Cipher

class Monoalphabetic(Cipher):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = []
    for ch in alpha:
        alpha_list.append(ch)