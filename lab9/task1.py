import random
import math


def miller_rabin(n, k=5):

    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
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


def generate_prime(bits=64):
    while True:
        n = random.getrandbits(bits)
        n |= (1 << bits - 1) | 1
        if miller_rabin(n):
            return n


def find_primitive_root(p):
    if p == 2:
        return 1

    factors = set()
    phi = p - 1
    n = phi

    for i in range(2, int(math.sqrt(phi)) + 1):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.add(n)

    while True:
        g = random.randrange(2, p)
        if all(pow(g, phi // factor, p) != 1 for factor in factors):
            return g


def generate_keys(bits=64):
    p = generate_prime(bits)

    g = find_primitive_root(p)

    x = random.randrange(2, p - 1)

    y = pow(g, x, p)

    return {
        'public_key': (p, g, y),
        'private_key': x
    }


def encrypt(message, public_key):
    p, g, y = public_key
    if message >= p:
        raise ValueError("Повідомлення занадто велике")

    k = random.randrange(2, p - 1)

    a = pow(g, k, p)
    b = (message * pow(y, k, p)) % p

    return (a, b)


def decrypt(ciphertext, private_key, p):

    a, b = ciphertext
    x = private_key


    s = pow(a, x, p)
    s_inv = pow(s, p - 2, p)

    return (b * s_inv) % p

def elgamal():
    print("Генерація ключів...")
    keys = generate_keys()
    p, g, y = keys['public_key']
    x = keys['private_key']

    print(f"p = {p}")
    print(f"g = {g}")
    print(f"y = {y}")
    print(f"x = {x}")
    message = 42
    print(f"\nПочаткове повідомлення: {message}")

    encrypted = encrypt(message, keys['public_key'])
    print(f"Зашифроване повідомлення: {encrypted}")

    decrypted = decrypt(encrypted, keys['private_key'], p)
    print(f"Розшифроване повідомлення: {decrypted}")

    assert message == decrypted, "Помилка: розшифроване повідомлення не співпадає з оригінальним!"
    print("\nТест успішний: шифрування та розшифрування працює коректно!")


if __name__ == "__main__":
    elgamal()