def phi(m):
    result = m
    p = 2
    while p * p <= m:
        if m % p == 0:
            # Якщо p є простим дільником m, виключаємо його з результату
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    # Якщо m залишився простим числом більше 1, враховуємо його
    if m > 1:
        result -= result // m
    return result

# Тест
m = 18
print(f"Значення функції Ейлера φ({m}) дорівнює {phi(m)}")
