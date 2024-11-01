

def gcdex(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0  # Повертає d, x, y

# Тест
a, b = 612, 342
d, x, y = gcdex(a, b)
print(f"d = {d}, x = {x}, y = {y}")


def inverse_element(a, n):
    d, x, _ = gcdex(a, n)
    if d != 1:
        return None  # Оборотного елемента не існує, якщо d ≠ 1
    return x % n  # x по модулю n — це обернений елемент

# Тест
a, n = 5, 18
inv = inverse_element(a, n)
print(f"Мультиплікативний обернений елемент для a = {a} по модулю n = {n} дорівнює {inv}")