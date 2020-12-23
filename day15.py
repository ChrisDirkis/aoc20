from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day15"
testing_file_name = data_file_name + "_test"

def part_1(filename, count):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        initial = [int(x) for x in file.read().split(",")]

        when_i_said = dict()
        say_next = 0

        for i, n in enumerate(initial):
            #print(f"step {i + 1}, speaking {n}")
            last = when_i_said.get(n, -1)
            when_i_said[n] = i
            say_next = 0 if last == -1 else i - last

        for i in range(len(initial), count):
            if i == count - 1:
                print(f"step {i + 1}, speaking {say_next}")
            last = when_i_said.get(say_next, -1)
            when_i_said[say_next] = i
            say_next = 0 if last == -1 else i - last


def part_2(filename, count):
    print(f"Part 2: {filename}")
    with open(filename) as file:        
        initial = [int(x) for x in file.read().split(",")]

        when_i_said = dict()
        say_next = 0

        for i, n in enumerate(initial):
            #print(f"step {i + 1}, speaking {n}")
            last = when_i_said.get(n, -1)
            when_i_said[n] = i
            say_next = 0 if last == -1 else i - last

        for i in range(len(initial), count):
            if i == count - 1:
                print(f"step {i + 1}, speaking {say_next}")
            last = when_i_said.get(say_next, -1)
            when_i_said[say_next] = i
            say_next = 0 if last == -1 else i - last

if __name__ == "__main__":
    part_1(testing_file_name, 10)
    part_1(data_file_name, 2020)
    part_2(testing_file_name, 30000000)
    part_2(data_file_name, 30000000)