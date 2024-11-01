def inverse_element(a, p):
    if a % p == 0:
        return None
    return pow(a, p - 2, p)

a, p = 5, 18
inv = inverse_element(a, p)
if inv is not None:
    print(f"Мультиплікативний обернений елемент для a = {a} по модулю p = {p} дорівнює {inv}")
else:
    print(f"Обернений елемент для a = {a} по модулю p = {p} не існує")

