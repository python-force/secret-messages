from caesar import Cipher

class Adfgvx(Cipher):
    ADFGVX = {
        "AA": "N", "AD": "A", "AF": "1", "AG": "C", "AV": "3", "AX": "H",
        "DA": "8", "DD": "T", "DF": "B", "DG": "2", "DV": "O", "DX": "M",
        "FA": "E", "FD": "5", "FF": "W", "FG": "R", "FV": "P", "FX": "D",
        "GA": "4", "GD": "F", "GF": "6", "GG": "G", "GV": "7", "GX": "I",
        "VA": "9", "VD": "J", "VF": "0", "VG": "K", "VV": "L", "VX": "Q",
        "XA": "S", "XD": "U", "XF": "V", "XG": "X", "XV": "Y", "XX": "Z",
    }

    def encrypt(self, message):
        message = message.upper().split()
        message = "".join(message)

        step = []
        for ch in message:
            for keys, values in self.ADFGVX.items():
                if ch == values:
                    step.append(keys)
        step = "".join(step)

        password = input("What is the password? ")
        x = len(step) // len(password)
        x_mod = len(step) % len(password)
        if x_mod != 0:
            x = x + 1

        rows = []
        for i in range(0, x):
            if x_mod != 0:
                if i == x:
                    rows.append(step[len(password) * i:])
                else:
                    rows.append(step[len(password) * i:len(password) * i + len(password)])
            else:
                rows.append(step[len(password) * i:len(password) * i + len(password)])

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

        sorted_list = []
        for key in sorted(dict):
            sorted_list.append(dict[key])
        return " ".join(sorted_list)

    def decrypt(self, message):
        secret = message.split()
        print(secret)
        password = input("Enter the Password: ")
        sorted_list = sorted(password)
        print(sorted_list)

        dict = {}
        for i in range(0, len(secret)):
            try:
                dict[sorted_list[i] + str(password.index(sorted_list[i]))] = secret[i]
            except:
                pass

        new_list = []
        for ch in password:
            key = ch + str(password.index(ch))
            if key in dict.keys():
                new_list.append(dict[key])
        whole_message = "".join(new_list)

        y = len(whole_message) // len(password)
        y_mod = len(whole_message) % len(password)
        if y_mod != 0:
            y = y + 1

        total_list = []
        for i in range(0, y):
            for item in new_list:
                try:
                    total_list.append(item[i])
                except:
                    pass
        total_list = "".join(total_list)

        double_list = []
        for i in range(0, len(total_list), 2):
            double_list.append(total_list[i:i + 2])

        message = []
        for item in double_list:
            if item in self.ADFGVX.keys():
                message.append(self.ADFGVX[item])
        message = "".join(message)
        return message