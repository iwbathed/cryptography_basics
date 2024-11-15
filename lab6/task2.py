
def gf_multiply(byte1, byte2):
    result = 0
    modulus = 0x1B
    for _ in range(8):
        if byte2 & 1:
            result ^= byte1

        if byte1 & 0x80:
            byte1 = (byte1 << 1) ^ modulus
        else:
            byte1 <<= 1

        byte2 >>= 1

    return result & 0xFF


if __name__ == "__main__":
    byte1 = 0x57
    byte2 = 0x83
    result = gf_multiply(byte1, byte2)
    print(f"57 * 83 = {result:02X}")
