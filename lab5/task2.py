import random

def miller_rabin(n, k=40):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True



def generate_prime(bits=1024):
    while True:
        num = random.getrandbits(bits) | (
                    1 << (bits - 1)) | 1
        if miller_rabin(num):
            return num

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def generate_keys(bits=1024):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537
    gcd, d, _ = extended_gcd(e, phi_n)

    if gcd != 1:
        raise ValueError("e and phi_n are not coprime")

    d = d % phi_n

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]


def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])


if __name__ == "__main__":

    public_key, private_key = generate_keys(bits=1024)
    print("Public key:", public_key)
    print("Private key:", private_key)

    message = "This is a secret message"
    print("Original message:", message)

    ciphertext = encrypt(public_key, message)
    print("Encrypted message:", ciphertext)
    print(len(ciphertext))

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message:", decrypted_message)