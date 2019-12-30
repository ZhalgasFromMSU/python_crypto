import argparse

from random import shuffle
from os.path import normpath

LENGTH = 256

def add_options(parser):
    parser.add_argument(
        '--mode',
        help='Choose working mode',
        required=True,
        choices={'encrypt', 'decrypt', 'genkey', 'break'},
    )
    parser.add_argument(
        '--output',
        '-o',
        default='output_file',
    )
    parser.add_argument(
        '--input',
        '-i',
        default='input_file',
    )
    parser.add_argument(
        '--key',
        '-k',
        default='key_file',
    )
    parser.add_argument(
        '--pool',
        '-p',
        default='pool_file',
    )

def gen_key(output_path):
    key = [i for i in range(LENGTH)]
    shuffle(key)
    with open(output_path, "bw") as out:
        out.write(bytes(key))

def ecnrypt(key_path, input_path, output_path):
    with open(key_path, "br") as key_inp,\
         open(input_path, "br") as inp,\
         open(output_path, "bw") as out:
        key = key_inp.read()
        out.write(bytes([key[i] for i in inp.read()]))

def decrypt(key_path, input_path, output_path):
    with open(key_path, "br") as key_inp,\
         open(input_path, "br") as inp,\
         open(output_path, "bw") as out:
        key = key_inp.read()
        reverse_key = [0 for i in range(LENGTH)]
        for key, val in enumerate(key):
            reverse_key[val] = key
        out.write(bytes([reverse_key[i] for i in inp.read()]))

def break_cipher(cipher_path, pool_path, output_path):
    with open(cipher_path, "br") as cip_text,\
         open(pool_path, "br") as pool,\
         open(output_path, "bw") as out:
        cip_dict = {i: 0 for i in range(LENGTH)}
        pool_dict = {i: 0 for i in range(LENGTH)}
        for byte in cip_text.read():
            cip_dict[byte] += 1
        for byte in pool.read():
            pool_dict[byte] += 1
        cip_freq_sorted = sorted(cip_dict.keys(), key=lambda key: cip_dict[key], reverse=True)
        pool_freq_sorted = sorted(pool_dict.keys(), key=lambda key: pool_dict[key], reverse=True)
        key_dict = {i: j for i, j in zip(pool_freq_sorted, cip_freq_sorted)}
        out.write(bytes([key_dict[i] for i in range(LENGTH)]))


def main(args):
    if args.mode == 'genkey':
        gen_key(normpath(args.key))
    elif args.mode == 'encrypt':
        ecnrypt(*map(normpath, (args.key, args.input, args.output)))
    elif args.mode == 'decrypt':
        decrypt(*map(normpath, (args.key, args.input, args.output)))
    elif args.mode == 'break':
        break_cipher(*map(normpath, (args.input, args.pool, args.output)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Multifunctional Caesar cipher')
    add_options(parser)
    main(parser.parse_args())
