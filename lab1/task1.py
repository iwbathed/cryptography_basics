

def encrypt(text, key_word_1, key_word_2):
    max_len = (len(key_word_1)) * (len(key_word_2))
    if len(text) > max_len:
        print(f"keys too short: message max length is {max_len}\ncurrent message length is {len(text)}")
    else:
        lst : list[list] = [[" "] * (len(key_word_1) + 1) for _ in range(len(key_word_2) + 1)]

        for i in range(len(key_word_1)):
            lst[0][i + 1] = key_word_1[i]


        for i in range(len(key_word_2)):
            lst[i+1][0] = key_word_2[i]

        r=0
        for i in range(len(key_word_1)):
            for j in range(len(key_word_2)):
                try:
                    lst[i+1][j+1] = text[r]
                    r += 1
                except IndexError:
                    break
        print("start matrix:")
        print_matrix(lst)

        sorted_key_word_1 = sorted(key_word_1)
        sorted_key_word_2 = sorted(key_word_2)
        res: list[list] = [[" "] * (len(key_word_1) + 1) for _ in range(len(key_word_2) + 1)]


        for i in range(len(res[0])):
            try:
                res[0][i+1] = sorted_key_word_1[i]
            except IndexError:
                    break

        for i in range(len(res)):
            try:
                res[i + 1][0] = sorted_key_word_2[i]
            except IndexError:
                break
        first_column = [row[0] for row in lst]

        for i in range(len(sorted_key_word_2)):
            index1 = first_column.index(sorted_key_word_2[i])
            for j in range(len(sorted_key_word_1)):
                index2 = lst[0].index(sorted_key_word_1[j])
                res[i+1][j+1] = lst[index1][index2]

        return res


def decrypt(matrix, key_word_1, key_word_2):
    res: list[list] = [[" "] * (len(key_word_1) + 1) for _ in range(len(key_word_2) + 1)]
    for i in range(len(key_word_2)):
        res[i+1][0] = key_word_2[i]

    for i in range(len(key_word_1)):
        res[0][i+1] = key_word_1[i]

    first_column = [row[0] for row in matrix]
    print(first_column)
    for i in range(len(key_word_2)):
        for j in range(len(key_word_1)):
            res[i+1][j+1] = matrix[first_column.index(key_word_2[i])][matrix[0].index(key_word_1[j])]

    return res


def matrix_to_str(matrix):
    res = ""
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            res += matrix[i+1][j+1]
    return res

def print_matrix(matrix):

    col_widths = [max(len(str(element)) for element in column) for column in zip(*matrix)]

    horizontal_line = "+".join("-" * (width + 2) for width in col_widths)
    horizontal_line = f"+{horizontal_line}+"

    print(horizontal_line)
    for row in matrix:
        row_str = " | ".join(f"{str(element).rjust(width)}" for element, width in zip(row, col_widths))
        print(f"| {row_str} |")
        print(horizontal_line)

    print()




if __name__ == "__main__":
    text = "hello, how are you? it is nice to meet you!"
    key_word_1 = "encrypt"
    key_word_2 = "decrypt"

    matrix = encrypt(text, key_word_1, key_word_2)
    print("encrypted matrix:")
    print_matrix(matrix)

    print("decrypted matrix:")
    decrypted_matrix = decrypt(matrix, key_word_1, key_word_2)
    print_matrix(decrypted_matrix)

    message = matrix_to_str(decrypted_matrix).strip()
    print(f"decrypted message:\"{message}\"")