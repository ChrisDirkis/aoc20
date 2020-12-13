import re
from typing import Tuple

def split_line(line: str) -> Tuple[int, int, str, str]:
    regex = r"(\d*)-(\d*) (.): (.*)$"
    match = re.match(regex, line)
    if not match:
        raise Exception("Line does not match format")

    low = int(match.group(1))
    high = int(match.group(2))
    char = match.group(3)
    password = match.group(4)

    return (low, high, char, password)


def is_valid_password_1(line: str) -> bool:
    (low, high, char, password) = split_line(line)
    num_char = sum(1 for c in password if c == char)
    return low <= num_char and high >= num_char

def is_valid_password_2(line: str) -> bool:
    (low, high, char, password) = split_line(line)
    return (password[low - 1] == char) ^ (password[high - 1] == char)


def part_1():
    with open("inputs/day2") as file:
        print(sum(is_valid_password_1(line) for line in file))

def part_2():
    with open("inputs/day2") as file:
        print(sum(is_valid_password_2(line) for line in file))


if __name__ == "__main__":
    part_1()
    part_2()