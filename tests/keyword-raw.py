def CipherString(keyword):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list=[]
    for ch in alpha:
        alpha_list.append(ch)

    keyword_list=[]
    for ch in keyword:
        keyword_list.append(ch)

    beta_list = alpha_list.copy()
    for ch in keyword_list:
        if ch in beta_list:
            beta_list.remove(ch)

    cipher_list = keyword_list + beta_list
    dict = {}
    for i in range(0, len(cipher_list)):
        dict[alpha_list[i]] = cipher_list[i]
    return(dict)

main_dict=CipherString("POTA")
phrase = "HELLO THERE"
phrase = phrase.split()
new_list=[]
for item in phrase:
    word = []
    for ch in item:
        for key, value in main_dict.items():
            if ch in value:
                word.append(key)
    word = "".join(word)
    new_list.append(word)
print(new_list)

main_dict=CipherString("POTA")
phrase = "KHOOB CKHSH"
phrase = phrase.split()

new_list=[]
for item in phrase:
    word = []
    for ch in item:
        for key, value in main_dict.items():
            if ch in key:
                word.append(value)
    word = "".join(word)
    new_list.append(word)
print(new_list)