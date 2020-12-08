def make_bit_seq(s: str) -> str:
    if not s.isascii():
        raise ValueError("Only ASCII characters allowed")
    return "".join(f"{ord(i):07b}" for i in s)


def norris_binary():
    message = input()
    answer = ""
    chars = [m for m in make_bit_seq(message)]
    i = 0
    while i < len(chars) - 1:
        nb = "0" if chars[i] == "1" else "00"
        answer += f"{nb} "
        j = 1
        while i < len(chars) - 1 and chars[i] == chars[i + 1]:
            j += 1
            i += 1
        i += 1
        answer += f"{'0' * j} "
    if i == len(chars) - 1:
        nb = "0" if chars[i] == "1" else "00"
        answer += f"{nb} 0"
    print(answer.strip())


if __name__ == '__main__':
    norris_binary()
