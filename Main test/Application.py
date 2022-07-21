from art import tprint
from collections import Counter
from pathlib import Path
from string import punctuation



def func(file_path):
    c = {}
    if Path(file_path).is_file():
        with open(file = file_path, mode = 'rt') as file:
            for line in file:
                for word in line.lower().split():
                    key = word.rstrip(punctuation)
                    c[key] = c.get(key, 0) + 1
    return c


def main():
    tprint('Func', font = 'cybermedum')
    print(func(file_path = input("\n Enter a file's path: ")))



if __name__ == '__main__':
    main()
