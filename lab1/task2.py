


abc = ['а', 'б', 'в', 'г','ґ', 'д', 'е', 'є', 'ж', 'з', 'и', "і", "ї", 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.isalpha() and char in abc:
            index = abc.index(char)
            encrypted_text += abc[ index + (shift - len(abc) * ((index + shift) // len(abc)))]

        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha()and char in abc:
            index = abc.index(char)
            decrypted_text += abc[index - (shift + len(abc) * ((index - shift) // len(abc)))]
        else:
            decrypted_text += char
    return decrypted_text


message = "Hello, світ!"
shift_value = 79

encrypted_message = encrypt(message, shift_value)
print("Зашифроване повідомлення:", encrypted_message) # Зашифроване повідомлення: hello, блфв!

decrypted_message = decrypt(encrypted_message, shift_value)
print("Розшифроване повідомлення:", decrypted_message) # Розшифроване повідомлення: hello, світ!
