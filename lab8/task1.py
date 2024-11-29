
import random


def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    s, r = 0, n - 1
    while r % 2 == 0:
        r //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, r, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_safe_prime(bits=512):
    while True:
        q = random.getrandbits(bits - 1) | 1
        if is_prime(q):
            p = 2 * q + 1
            if is_prime(p):
                return p, q


def is_generator(g, p):
    return pow(g, (p - 1) // 2, p) != 1


def find_generator(p):
    while True:
        g = random.randint(2, p - 2)
        if is_generator(g, p):
            return g


def diffie_hellman_exchange(p, g):
    a = random.randint(1, p - 2)
    b = random.randint(1, p - 2)

    A = pow(g, a, p)
    B = pow(g, b, p)
    secret_a = pow(B, a, p)
    secret_b = pow(A, b, p)

    assert secret_a == secret_b, "Секрети не збігаються!"

    return secret_a


if __name__ == "__main__":

    p, q = generate_safe_prime()
    g = find_generator(p)

    print(f"Просте число p: {p}")
    print(f"Генератор g: {g}")


    shared_secret = diffie_hellman_exchange(p, g)
    print(f"Спільний секретний ключ: {shared_secret}")








