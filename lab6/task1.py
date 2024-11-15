def mul02(byte):
    byte = byte & 0xFF
    result = byte << 1
    if byte & 0x80:
        result ^= 0x1B
    return result & 0xFF

def mul03(byte):
    return mul02(byte) ^ byte


if __name__ == "__main__":
    byte1 = 0xD4
    result1 = mul02(byte1)
    print(f"D4 * 02 = {result1:02X} (очікується B3)")

    byte2 = 0xBF
    result2 = mul03(byte2)
    print(f"BF * 03 = {result2:02X} (очікується DA)")