adfgvx = {
    "AA": "N", "AD": "A", "AF": "1", "AG": "C", "AV": "3", "AX": "H",
    "DA": "8", "DD": "T", "DF": "B", "DG": "2", "DV": "O", "DX": "M",
    "FA": "E", "FD": "5", "FF": "W", "FG": "R", "FV": "P", "FX": "D",
    "GA": "4", "GD": "F", "GF": "6", "GG": "G", "GV": "7", "GX": "I",
    "VA": "9", "VD": "J", "VF": "0", "VG": "K", "VV": "L", "VX": "Q",
    "XA": "S", "XD": "U", "XF": "V", "XG": "X", "XV": "Y", "XX": "Z",
}

message = "Get to the Chopaaah"
message = message.upper().split()
message = "".join(message)
print(message)

step = []

for ch in message:
    for keys, values in adfgvx.items():
        if ch == values:
            step.append(keys)
print(step)
step2 = "".join(step)

password = "PREDATO"
x = len(step2) // len(password)
x_mod = len(step2) % len(password)
if x_mod != 0:
    x = x + 1

rows = []
for i in range(0, x):
    if x_mod != 0:
        if i == x:
            rows.append(step2[len(password) * i:])
        else:
            rows.append(step2[len(password) * i:len(password) * i + len(password)])
    else:
        rows.append(step2[len(password) * i:len(password) * i + len(password)])
print(rows)

dict = {}
for i in range(0, len(password)):
    list = []
    for item in rows:
        try:
            if item[i]:
                list.append(item[i])
        except:
            pass
    final_string = "".join(list)
    dict[password[i] + str(i)] = final_string

print(dict)

sorted_list = []
for key in sorted(dict):
    sorted_list.append(dict[key])
print(" ".join(sorted_list))

secret = "DDAD ADGAX FVAVA DXDD GDFVA GDAFD DAXA"
secret = secret.split()
password = "PREDATO"
sorted_list = sorted(password)
print(sorted_list)

dict={}
for i in range(0, len(secret)):
    try:
        dict[sorted_list[i] + str(password.index(sorted_list[i]))] = secret[i]
    except:
        pass
print(dict)

new_list=[]
for ch in password:
    key = ch + str(password.index(ch))
    if key in dict.keys():
        new_list.append(dict[key])
whole_message = "".join(new_list)
print(new_list)

x = "".join(new_list)
print(len(x)/7)
print(len(x))

password = "PREDATO"
y = len(x) // len(password)
y_mod = len(x) % len(password)
if y_mod != 0:
    y = y+1

total_list = []
for i in range(0, y):
    for item in new_list:
        try:
            total_list.append(item[i])
        except:
            pass
total_list = "".join(total_list)
print(total_list)

double_list = []
for i in range(0, len(total_list), 2):
    double_list.append(total_list[i:i+2])
print(double_list)

message=[]
for item in double_list:
    if item in adfgvx.keys():
        message.append(adfgvx[item])
message = "".join(message)
print(message)

