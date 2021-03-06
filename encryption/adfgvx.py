from encryption.cipher import Cipher


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
        """
        Encryption method, where message characters are changed based on
        ADFGVX dictionary. Asks for password which has to have unique characters.
        Creates columns of characters which are mixed by the password sorted A-Z and
        being returned
        Full Algorithm here: https://en.wikipedia.org/wiki/ADFGVX_cipher
        :param message:
        :return:
        """
        message = message.upper().split()
        message = "".join(message)

        # adds keys to step list
        step = []
        for ch in message:
            for keys, values in self.ADFGVX.items():
                if ch == values:
                    step.append(keys)
        step = "".join(step)

        # asks users for password
        password = input("What is the password? All characters must be unique.")
        for ch in password:
            occurences = password.count(ch)
            if occurences > 1:
                print("Your password includes duplicates. They are not unique characters.")
                return None
            else:
                x = len(step) // len(password)
                x_mod = len(step) % len(password)
                if x_mod != 0:
                    x = x + 1

                # based on the mod result, rows are being created
                rows = []
                for i in range(0, x):
                    if x_mod != 0:
                        if i == x:
                            rows.append(step[len(password) * i:])
                        else:
                            rows.append(step[len(password) * i:len(password) * i + len(password)])
                    else:
                        rows.append(step[len(password) * i:len(password) * i + len(password)])

                # creating columns of strings
                dict = {}
                for i in range(0, len(password)):
                    list = []
                    for item in rows:
                        try:
                            if item[i]:
                                list.append(item[i])
                        except:
                            continue
                    final_string = "".join(list)
                    dict[password[i] + str(i)] = final_string

                # sort the list of columns based on the password
                sorted_list = []
                for key in sorted(dict):
                    sorted_list.append(dict[key])

                return " ".join(sorted_list)

    def decrypt(self, message):
        """
        Decryption method, where based on the password, which characters are being sorted.
        Creating keys and then creating the whole string. Store all double keys in the list and
        compare with main dictionary to get the values.
        Full Algorithm here: https://en.wikipedia.org/wiki/ADFGVX_cipher
        """
        secret = message.split()
        password = input("Please enter the password for the message: ")
        for ch in password:
            occurences = password.count(ch)
            if occurences > 1:
                print("Your password includes duplicates. It it not correct")
                return None
            else:
                sorted_list = sorted(password)

                # Dictionary with keys and values bases on the password and indexes
                dict = {}
                for i in range(0, len(secret)):
                    try:
                        dict[sorted_list[i] + str(password.index(sorted_list[i]))] = secret[i]
                    except:
                        continue

                # Sorting all characters and combine all together
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

                # Sorting the columns / rows to make the original string
                total_list = []
                for i in range(0, y):
                    for item in new_list:
                        try:
                            total_list.append(item[i])
                        except:
                            continue
                total_list = "".join(total_list)

                # Creating the keys (double keys)
                double_list = []
                for i in range(0, len(total_list), 2):
                    double_list.append(total_list[i:i + 2])

                # Message created from the main dictionary based on double_list keys
                message = []
                for item in double_list:
                    if item in self.ADFGVX.keys():
                        message.append(self.ADFGVX[item])
                message = "".join(message)
                return message
