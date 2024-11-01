def inverse_element(a, p):
    if a % p == 0:
        return None  # Оборотного елемента не існує, якщо a і p не взаємно прості
    # Знаходимо обернений елемент за формулою a^(p-2) mod p
    return pow(a, p - 2, p)

# Тест
a, p = 5, 18
inv = inverse_element(a, p)
if inv is not None:
    print(f"Мультиплікативний обернений елемент для a = {a} по модулю p = {p} дорівнює {inv}")
else:
    print(f"Обернений елемент для a = {a} по модулю p = {p} не існує")

