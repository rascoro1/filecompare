import os
from .funcmodule import md5
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compare file content in directory')
    parser.add_argument('--raw', dest='raw', action='store_true', help='easily parsable results')
    parser.add_argument('--hash', action='store', type=str, default="md5", help='available hash algos: md5')
    parser.add_argument('directory', type=str, help='dir to search, for all similar files')
    return parser.parse_args()

def main():
    args = parse_args()
    hashes = {}
    dirname = args.directory.rstrip("/")

    # Get all files in all sun directories
    for dir, dirname, filename in os.walk(dirname):
        for f in filename:
            full_path = dir + "/" + f
            hash = md5(full_path)
            if hash in hashes:
                hashes[hash].append(full_path)
            else:
                hashes[hash] = [full_path]

    for k, v in hashes.items():
        if len(v) > 1:
            print("{}: ".format(len(v)) + "\n\t-".join(v))



if __name__ == "__main__":
    main()

