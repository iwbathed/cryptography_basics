import random

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result



def miller_rabin(p, k):
    if p <= 1:
        return False, 0
    if p == 2:
        return True, 1
    if p % 2 == 0:
        return False, 0


    d = p - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, p - 2)
        x = modular_exponentiation(a, d, p)
        if x == 1 or x == p - 1:
            continue

        for _ in range(s - 1):
            x = modular_exponentiation(x, 2, p)
            if x == p - 1:
                break
        else:
            return False, 1

    return True, 1

p = 1000000007
k = 20
is_prime, probability = miller_rabin(p, k)
print(
    f"Число {p} є {'простим' if is_prime else 'складеним'}, ймовірність простоти: {probability}")