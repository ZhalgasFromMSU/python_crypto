#Возвращает спискок, где для каждого файла хранится
#содержимое файла без whitespace
def read_strip(*file_names):
    return [''.join(open(file, 'r', encoding='utf-8').read().split()) for file in file_names]


def letter_parser(*file_names):
    return {l:text.count(l) for text in read_strip(*file_names) for l in set(text)}


def main():
    print("Введите названия файлов через пробел, в одной строке.")
    file_names = input().split()
    print(letter_parser(*file_names))


if __name__ == "__main__":
    main()
