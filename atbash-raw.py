alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_list = []
for ch in alpha:
    alpha_list.append(ch)

backwards_list = alpha_list[::-1]
print(alpha_list)
print(backwards_list)

dict = {}
for i in range(0, len(alpha_list)):
    dict[alpha_list[i]] = backwards_list[i]
print (dict)

phrase = "get to the chopaaaah"
phrase = phrase.upper().split()
new_list=[]
for item in phrase:
    word = []
    for ch in item:
        for key, value in dict.items():
            if ch in value:
                word.append(key)
    word = "".join(word)
    new_list.append(word)
print(new_list)


phrase = "TVG GL GSV XSLKZZZZZS"
phrase = phrase.upper().split()

new_list=[]
for item in phrase:
    word = []
    for ch in item:
        for key, value in dict.items():
            if ch in key:
                word.append(value)
    word = "".join(word)
    new_list.append(word)
print(new_list)