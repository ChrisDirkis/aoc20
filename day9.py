from itertools import *
from functools import *
from math import * 
import re

from typing import *

input_file = "inputs/day9"
pre = 25

def first_invalid(nums, preamble):
    for i, v in enumerate(nums[preamble:]):
        to_check = nums[i:i + preamble]
        possible = set(a + b for a, b in product(to_check, to_check) if a != b)
        if not v in possible:
            return(v)

def part_1():
    with open(input_file) as file:
        nums = [int(i) for i in file.readlines()]
        print(first_invalid(nums, pre))
        pass

def part_2():
    with open(input_file) as file:
        nums = [int(i) for i in file.readlines()]
        invalid = first_invalid(nums, pre)

        for i in range(len(nums)):
            j = 0
            while True:
                test = nums[i:i+j]
                s = sum(test)
                if s == invalid:
                    print(min(test) + max(test))
                    return
                elif s > invalid:
                    break
                j += 1
                if i + j > len(nums):
                    break
            
        pass

if __name__ == "__main__":
    part_1()
    part_2()