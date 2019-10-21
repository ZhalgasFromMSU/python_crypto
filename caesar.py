def cyclic_jump(letter, letter_ord):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        return chr((letter_ord - ord('a')) % 26 + ord('a'))
    return chr((letter_ord - ord('A')) % 26 + ord('A'))


def encrypt(text, padding=3):
    return ''.join([cyclic_jump(x, ord(x) + padding) for x in text])


def decrypt(text, padding=3):
    return ''.join([cyclic_jump(x, ord(x) - padding) for x in text])


def main():
    print("Введите текст (большие и маленькие буквы латинского алфавита)")
    text = input()
    print("Введите смещение (любое число)")
    padding = int(input())
    print("Введите 1, чтобы зашифровать и 2, чтобы расшифровать")
    mode = int(input())
    if mode == 1:
        print(encrypt(text, padding=padding))
    else:
        print(decrypt(text, padding=padding))


if __name__ == "__main__":
    main()
