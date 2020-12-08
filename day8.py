from itertools import *
from functools import *
from math import * 
import re

from typing import *

input_file = "inputs/day8"

def make_machine(string):
    return [(i, int(v)) for i, v in re.findall(r"(.{3}) ([-+]\d*)\n", string)]

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
        instr, value = machine[ptr]
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
        machine = make_machine(file.read())
        acc, _ = run_until_cycle(machine)
        print(acc)

def part_2():
    with open(input_file) as file:
        machine = make_machine(file.read())
        for i, instr in enumerate(machine):
            if instr[0] != "acc":
                machine[i] = ("jmp" if instr[0] == "nop" else "nop", instr[1])

                acc, ptr = run_until_cycle(machine)
                if ptr == len(machine):
                    print(acc)
                    break

                machine[i] = instr

if __name__ == "__main__":
    part_1()
    part_2()