from itertools import *
from functools import *
from math import * 
import re

from typing import *

input_file = "inputs/day8"

def run_until_cycle(machine):
    acc = 0
    ptr = 0
    seen = set()
    while True:
        if ptr in seen:
            break
        if ptr >= len(machine):
            break
        seen.add(ptr)
        instr, value = re.match(r"(.{3}) ([-+]\d*)$", machine[ptr]).groups()
        value = int(value)
        if instr == "nop":
            ptr += 1
        elif instr == "acc":
            acc += value
            ptr += 1
        elif instr == "jmp":
            ptr += value
    return (acc, ptr)
            

def part_1():
    with open(input_file) as file:
        lines = file.readlines()
        acc, _ = run_until_cycle(lines)
        print(acc)

def part_2():
    with open(input_file) as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            flag = False
            if line.startswith("jmp"):
                lines[i] = line.replace("jmp", "nop")
                flag = True
            elif line.startswith("nop"):
                lines[i] = line.replace("nop", "jmp")
                flag = True
            
            if flag:
                acc, ptr = run_until_cycle(lines)
                if ptr == len(lines):
                    print(acc)
                    break

                lines[i] = line

if __name__ == "__main__":
    part_1()
    part_2()