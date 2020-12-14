from itertools import *
from functools import *
from math import * 
import re

from typing import *

data_file_name = "inputs/day14"
testing_file_name = data_file_name + "_test"

powers = [2 ** i for i in range(36)]

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        data = dict()
        z_mask = 0
        o_mask = 0
        for line in file:
            if line[:3] == "mem":
                addr, value = re.match(r"^mem\[(\d+)] = (\d+)$", line).groups()
                data[int(addr)] = (int(value) | o_mask) & ~z_mask
            else:
                mask = line[7:]
                z_mask = sum(powers[35 - i] for i, v in enumerate(mask) if v == "0") 
                o_mask = sum(powers[35 - i] for i, v in enumerate(mask) if v == "1") 
        print(sum(data.values()))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        data = dict()
        o_mask = 0
        floating = []
        for line in file:
            if line[:3] == "mem":
                addr, value = re.match(r"^mem\[(\d+)] = (\d+)$", line).groups()
                addr = (int(addr) | o_mask)
                for config in floating:
                    modified_addr = addr
                    for bit in config:
                        if bit > 0:
                            modified_addr &= ~(1 << (bit - 1))
                        else:
                            modified_addr |= 1 << (-bit - 1)
                    data[modified_addr] = int(value)
                
            else:
                mask = line[7:]
                o_mask = sum(powers[35 - i] for i, v in enumerate(mask) if v == "1") 
                floating = list(product(*([(35 - i) + 1, -(35 - i) - 1] for i, v in enumerate(mask) if v == "X")))

        print(sum(data.values()))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)