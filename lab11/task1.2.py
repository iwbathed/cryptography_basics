def point_addition(P, Q, a, p):
    if P[0] is None:
        return Q
    if Q[0] is None:
        return P

    x1, y1 = P
    x2, y2 = Q
    if x1 != x2:
        lam = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    else:
        if y1 == p - y2:
            return (None, None)

        lam = ((3 * x1 ** 2 + a) * pow(2 * y1, -1, p)) % p

    x3 = (lam ** 2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

def point_multiplication(G, n, a, p):
    R = (None, None)
    Q = G

    while n:
        if n & 1:
            R = point_addition(R, Q, a, p)
        Q = point_addition(Q, Q, a, p)
        n >>= 1
    return R


def find_point_order(G, a, p):
    max_order = p + 1 + int((2 * (p ** 0.5)))

    for n in range(1, max_order + 1):
        result = point_multiplication(G, n, a, p)
        if result[0] is None:
            return n
    return None

a = 1
p = 23
G = (17, 20)

order = find_point_order(G, a, p)
print(f"Порядок точки {G} на кривій y^2 = (x^3 + {a}x + 1) mod {p}: {order}")