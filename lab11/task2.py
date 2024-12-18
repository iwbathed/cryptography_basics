

from random import randint

a = 1
b = 1
p = 23
G = (17, 20)

def point_addition(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 == y2:
        if y1 == 0:
            return None
        lam_numerator = (3 * x1 * x1 + a)
        lam_denominator = 2 * y1
        inv_denominator = mod_inverse(lam_denominator, p)
        if inv_denominator is None:
            return None
        lam = (lam_numerator * inv_denominator) % p
    else:
        if x1 == x2:
            return None
        lam_numerator = y2 - y1
        lam_denominator = x2 - x1
        inv_denominator = mod_inverse(lam_denominator, p)
        if inv_denominator is None:
            return None
        lam = (lam_numerator * inv_denominator) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3) if is_on_curve((x3, y3)) else None

def mod_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = egcd(b % a, a)
            return gcd, y - (b // a) * x, x
    a = a % m
    gcd, x, _ = egcd(a, m)
    if gcd != 1:
        return None
    return x % m

def scalar_multiply( k, P):
    R = None
    Q = P
    k = k % p
    while k:
        if k & 1:
            R = point_addition(R, Q)
            if R is None:
                raise ValueError("точка на нескінченності")
        Q = point_addition(Q, Q)
        if Q is None:
            raise ValueError("точка на нескінченності")
        k >>= 1
    return R

def point_negation(P):
    if P is None:
        return None
    x, y = P
    return (x, (-y) % p)

def is_on_curve(P):
    if P is None:
        return True
    x, y = P
    left = (y * y) % p
    right = (x ** 3 + a * x + b) % p
    return left == right



def generate_key_pair():
    private_key = randint(2, p - 2)
    public_key = scalar_multiply(private_key, G)
    return private_key, public_key

def encrypt(message_point, public_key):
    k = randint(2, p - 2)
    C1 = scalar_multiply(k, G)
    shared_secret = scalar_multiply(k, public_key)
    C2 = point_addition(message_point, shared_secret)
    return C1, C2

def decrypt(C1, C2, private_key):
    shared_secret = scalar_multiply(private_key, C1)
    message_point = point_addition(C2, point_negation(shared_secret))
    return message_point

def main():
    assert is_on_curve(G), "точка не на кривій"
    private_1, public_1 = generate_key_pair()
    private_2, public_2 = generate_key_pair()
    print("приватний ключ 1:", private_1)
    print("публічний ключ 1:", public_1)
    print("приватний ключ 2:", private_2)
    print("публічний ключ 2:", public_2)

    message_point = (1, 16)
    C1, C2 = encrypt(message_point, public_2)

    print("шифр C1:", C1)
    print("шифр C2:", C2)
    decrypted_point = decrypt(C1, C2, private_2)

    print("розшифрована точка:", decrypted_point)
    assert decrypted_point == message_point, "помилка розшифрування"


if __name__ == "__main__":
    main()
