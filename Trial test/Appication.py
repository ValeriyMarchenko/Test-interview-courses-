from pathlib import Path
from art import tprint

def wordCount(file_path):
    if Path(file_path).is_file():
        with open(file = file_path, mode = 'rt') as file:
            data = file.read()
            words = data.split()

        return f'Number of words in text file : {len(words)}'


def main():
    tprint('Word Counter', font = 'cybermedum')
    print(wordCount(file_path = input("\n Enter a file's path: ")))


if __name__ == '__main__':
    main()
