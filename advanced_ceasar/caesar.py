from random import shuffle

#Принимает список и для него строит перестановку
def gen_transposition(a):
    shuffle(a)
    return a


def main():
    with open("test.o", "rb") as f:
        byte = f.read(1)
        while byte:
            print(byte)
            byte = f.read(1)


if __name__ == "__main__":
    print(main())
