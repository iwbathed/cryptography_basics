import random

abc = ['а', 'б', 'в', 'г','ґ', 'д', 'е', 'є', 'ж', 'з', 'и', "і", "ї", 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']



# abc_dict = dict()
# start_number = 1
# for letter in abc:
#     numbers = [start_number, start_number+2]
#     start_number += 3
#     abc_dict[letter] = [str(number) if number > 9 else "0" + str(number) for number in numbers]
#
# print(abc_dict)

abc_dict = {'а': ['01', '03'], 'б': ['04', '06'], 'в': ['07', '09'], 'г': ['10', '12'], 'ґ': ['13', '15'], 'д': ['16', '18'], 'е': ['19', '21'], 'є': ['22', '24'], 'ж': ['25', '27'], 'з': ['28', '30'], 'и': ['31', '33'], 'і': ['34', '36'], 'ї': ['37', '39'], 'й': ['40', '42'], 'к': ['43', '45'], 'л': ['46', '48'], 'м': ['49', '51'], 'н': ['52', '54'], 'о': ['55', '57'], 'п': ['58', '60'], 'р': ['61', '63'], 'с': ['64', '66'], 'т': ['67', '69'], 'у': ['70', '72'], 'ф': ['73', '75'], 'х': ['76', '78'], 'ц': ['79', '81'], 'ч': ['82', '84'], 'ш': ['85', '87'], 'щ': ['88', '90'], 'ь': ['91', '93'], 'ю': ['94', '96'], 'я': ['97', '99']}


def encrypt(message:str, encoding_dict:dict):
    message = message.lower()
    encrypted = ""
    for letter in message:
        if letter.isdigit():
            encrypted += abc[int(letter)]
        elif letter in abc:
            encrypted += encoding_dict[letter][random.randint(0, 1)]
        else:
            encrypted += letter
    return encrypted

def decrypt(encrypted_message:str, encoding_dict:dict):
    res = ""
    i = 0
    while i < len(encrypted_message):
        if encrypted_message[i].isdigit():
            number = encrypted_message[i]+encrypted_message[i+1]
            i += 1
            for key, values in encoding_dict.items():
                if number in values:
                    res += key
                    break
        elif encrypted_message[i] in abc:
            res += str(abc.index(encrypted_message[i]))
        else:
            res += encrypted_message[i]
        i += 1
    return res

if __name__ == "__main__":
    message = "Привіт, 002, how are you?"
    encrypted_message = encrypt(message, abc_dict)
    print(encrypted_message)

    decrypted_message = decrypt(encrypted_message, abc_dict)
    print(decrypted_message)
