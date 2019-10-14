def letter_parser(*file_names):
    letter_frequency = dict()
    for file in file_names:
        with open(file, 'r', encoding='utf-8') as f:
            for letter in ''.join((''.join(f)).split()): # Избавляюсь от whitespace
                if not letter in letter_frequency:
                    letter_frequency[letter] = 1
                else:
                    letter_frequency[letter] += 1
    return letter_frequency


def main():
    print("Введите названия файлов через пробел, в одной строке.")
    file_names = input().split()
    print(letter_parser(*file_names))


if __name__ == "__main__":
    main()
