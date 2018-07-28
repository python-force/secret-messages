import string
import random

alphabet = string.ascii_uppercase
alphabet_list = []
for ch in alphabet:
    alphabet_list.append(ch)
print(alphabet_list)
"""
Original Table
main_dict = {
        "A": (0, 26), "B": (1, 27), "C": (2, 28), "D": (3, 29), "E": (4, 30), "F": (5, 31),
        "G": (6, 32), "H": (7, 33), "I": (8, 34), "J": (9, 35), "K": (10, 36), "L": (11, 37),
        "M": (12, 38), "N": (13, 39), "O": (14, 40), "P": (15, 41), "Q": (16, 42), "R": (17, 43),
        "S": (18, 44), "T": (19, 45), "U": (20, 46), "V": (21, 47), "W": (22, 48), "X": (23, 49),
        "Y": (24, 50), "Z": (25, 25)
    }
"""
main_dict = {
    "A": (0, 27), "B": (1, 28), "C": (2, 29), "D": (3, 30), "E": (4, 31), "F": (5, 32),
    "G": (6, 33), "H": (7, 34), "I": (8, 35), "J": (9, 36), "K": (10, 37), "L": (11, 38),
    "M": (12, 39), "N": (13, 40), "O": (14, 41), "P": (15, 42), "Q": (16, 43), "R": (17, 44),
    "S": (18, 45), "T": (19, 46), "U": (20, 47), "V": (21, 48), "W": (22, 49), "X": (23, 50),
    "Y": (24, 51), "Z": (25, 52), " ": (26, 26)
}

# message = "this is secret"

#message = message.upper().split()
#message = "".join(message)
message = "PREDATOR IS REAL"
message_list=[]
for ch in message:
    message_list.append(main_dict[ch][0])

print(message_list)

#random key

random_otp = [random.choice(alphabet_list) for _ in range(len(message))]
print ("".join(random_otp))
for i, item in enumerate(random_otp):
    random_otp[i] = main_dict[item][0]

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
    if item > 26:
        for key, value in main_dict.items():
            if value[1] == item:
                math_list[i] = key
    else:
        for key, value in main_dict.items():
            if value[0] == item:
                math_list[i] = key

print(math_list)
print("".join(math_list))



print("=====================")

message = "".join(math_list)

#message = message.upper().split()
#message = "".join(message)
message_list=[]
for ch in message:
    message_list.append(main_dict[ch][0])

print(message_list)
print(random_otp)

math_list = []
for i, item in enumerate(message_list):
    if message_list[i] >= random_otp[i]:
        x = message_list[i] - random_otp[i]
        for key, value in main_dict.items():
            if value[0] == x:
                math_list.append(key)
    else:
        for key, value in main_dict.items():
            if item == value[0]:
                x = value[1] - random_otp[i]
                for key, value in main_dict.items():
                    if value[0] == x:
                        math_list.append(key)
print(math_list)
print("".join(math_list))
