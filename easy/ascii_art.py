import re


def get_index(line: str) -> list:
    line = re.sub(r"\W", "?", line)
    alphabet = "abcdefghijklmnopqrstuvwxyz?"
    return [alphabet.index(token.lower()) for token in line]


def split_line(line: str, length: int) -> list:
    lines = [line[i:i + length] for i in range(0, len(line), length)]
    return lines


def write_ascii_art(length: int, height: int, word: str):
    row = [input() for i in range(height)]
    sub_word = [split_line(letter, length) for letter in row]
    ndx = get_index(word)
    lines = []
    for sw in sub_word:
        lines.append("".join([sw[n] for n in ndx]))
    for line in lines:
        print(line)


if __name__ == '__main__':
    l = int(input())
    h = int(input())
    t = input()
    write_ascii_art(l, h, t)


