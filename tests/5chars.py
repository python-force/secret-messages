message = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "]", "[", "?"]
message = "".join(message)
block_list = []
for i in range(0, len(message), 5):
    block_list.append(message[i:i+5])
print(block_list)

text = "KQJML XJEER E#TX! NKPRS FSOCR ECYPX S"
print(text.replace(" ",""))

list1 = ['g','e','e','k','s']
print("".join(list1))

