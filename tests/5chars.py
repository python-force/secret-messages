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

list = ['Z', 'X', 'I', 'D', 'E', 'A', 'S', 'O', 'A', 'N', 'V', 'O', ' ', 'L', 'L', 'P', 'R', 'B', 'Z', 'S', 'F', 'I', 'R', 'Y', 'N', ' ', 'Y', 'Z', 'I', 'Q']
list = "".join(list)
print(list)


text = "hello"

for ch in text:
    occurences = text.count(ch)
    if occurences > 1:
        print(ch)
        print("not good")



