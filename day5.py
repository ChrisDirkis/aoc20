from itertools import *
from functools import *
from math import * 
import re

from typing import *

input_file = "inputs/day5"

def get_seat_rc(b_pass):
    vals = [64, 32, 16, 8, 4, 2, 1]
    row = sum(r for r, v in zip(vals, (b == "B"  for b in b_pass[:7])) if v)
    col = sum(c for c, v in zip(vals[-3:], (b == "R" for b in b_pass[7:10])) if v)
    return (row, col)

def get_seat_id(b_pass):
    r, c = get_seat_rc(b_pass)
    return 8 * r + c

def part_1():
    with open(input_file) as file:
        print(max(get_seat_id(line) for line in file.readlines()))
        pass

def part_2():
    with open(input_file) as file:
        passes = set(get_seat_id(line) for line in file.readlines())
        print(sorted(passes))
        started = False
        i = 0
        while True:
            if not started:
                if i in passes:
                    started = True
                    print(f"started at {i}")

            else:
                if (i not in passes) and (i-1 in passes) and (i+1 in passes):
                    print(i)
                    return
            i += 1
        pass

if __name__ == "__main__":
    part_1()
    part_2()