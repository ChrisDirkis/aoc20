from itertools import *
from functools import *
from math import *
import re

from typing import *

input_file = "inputs/day4"
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part_1():
    with open(input_file) as file:
        valid = 0
        current_passport: Set[str] = set()
        for line in file.readlines():
            if len(line.strip()) == 0:
                is_valid = all(field in current_passport for field in required)
                if is_valid:
                    valid += 1
                current_passport = set()
                continue
            
            for field in re.findall(r"(\w\w\w):\S+\s", line):
                current_passport.add(field)

        print(valid)


def part_2():
    with open(input_file) as file:        
        valid = 0
        current_passport: Dict[str, str] = dict()
        for line in file.readlines():
            if len(line.strip()) == 0:
                testing = current_passport
                current_passport = dict()

                if not all(field in testing for field in required):
                    continue

                if not (1920 <= int(testing["byr"]) <= 2002):
                    continue

                if not (2010 <= int(testing["iyr"]) <= 2020):
                    continue

                if not (2020 <= int(testing["eyr"]) <= 2030):
                    continue

                if not re.match(r"\d\d\d\d\d\d\d\d\d$", testing["pid"]):
                    continue

                if not testing["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                    continue

                if not re.match(r"#[\da-f][\da-f][\da-f][\da-f][\da-f][\da-f]$", testing["hcl"]):
                    continue

                if not re.match(r"\d+(cm|in)$", testing["hgt"]):
                    continue

                if testing["hgt"].endswith("cm"):
                    if not re.match(r"\d\d\dcm$", testing["hgt"]) or not (150 <= int(testing["hgt"][:3]) <= 193):
                        continue
                else:
                    if not re.match(r"\d\din$", testing["hgt"]) or not (59 <= int(testing["hgt"][:2]) <= 76):
                        continue

                valid += 1
                continue
            
            for field in re.findall(r"(\w\w\w):(\S+)\s", line):
                current_passport[field[0]] = field[1]

        print(valid)

if __name__ == "__main__":
    part_1()
    part_2()