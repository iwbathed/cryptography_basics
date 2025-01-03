
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]


FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]



S_BOX = [
    [[14, 4, 13, 1], [2, 15, 11, 8], [3, 10, 6, 12], [5, 9, 0, 7]],
    [[0, 15, 7, 4], [14, 2, 13, 1], [10, 6, 12, 11], [9, 5, 3, 8]]
]



def permute(block, table):

    if len(block) != 64:
        raise ValueError("Block length must be 64 bits.")

    return ''.join(block[i - 1] for i in table)



def split_block(block):
    return block[:32], block[32:]


def expand_block(block, table):
    return ''.join(block[i - 1] for i in table)


def feistel_function(right, subkey):
    expanded = expand_block(right, EXPANSION_TABLE)
    xored = bin(int(expanded, 2) ^ int(subkey, 2))[2:].zfill(48)
    return xored[:32]

def generate_subkeys(key):
    binary_key = ''.join(f"{ord(c):08b}" for c in key)
    return [binary_key] * 16


def des_encrypt(plain_text, key):
    binary_plaintext = ''.join(f"{ord(c):08b}" for c in plain_text)
    subkeys = generate_subkeys(key)  # згенерувати підключі
    permuted_text = permute(binary_plaintext, IP)
    left, right = split_block(permuted_text)


    for i in range(16):
        new_right = bin(int(left, 2) ^ int(feistel_function(right, subkeys[i]), 2))[2:].zfill(32)
        left, right = right, new_right

    final_block = permute(right + left, FP)
    return final_block


def des_decrypt(cipher_text, key):
    subkeys = generate_subkeys(key)
    permuted_text = permute(cipher_text, IP)
    left, right = split_block(permuted_text)


    for i in range(15, -1, -1):
        new_left = bin(int(right, 2) ^ int(feistel_function(left, subkeys[i]), 2))[2:].zfill(32)
        right, left = left, new_left

    final_block = permute(right + left, FP)
    return final_block


plain_text = "12345768" # BC61A8
key = "abcdefgh"

print("Plaintext:", plain_text)

cipher = des_encrypt(plain_text, key)
print("Ciphertext:", cipher)

decrypted = des_decrypt(cipher, key)
print("Decrypted:", ''.join(chr(int(decrypted[i:i+8], 2)) for i in range(0, 64, 8)))




