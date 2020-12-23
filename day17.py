from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day17"
testing_file_name = data_file_name + "_test"


def add_coords(a, b):
    return tuple(z + o for z, o in zip(a, b))


def neighbours(data, coord):
    step = [-1, 0, 1]
    offsets = product(*(step for _ in range(len(coord))))
    s = 0
    for offset in offsets:
        s += 1 if add_coords(coord, offset) in data else 0

    return s - (1 if coord in data else 0)

def all_neighbour_coords(data):
    _c = next(iter(data))
    step = [-1, 0, 1]
    offsets = list(product(*(step for _ in range(len(_c)))))
    n = set()
    for c in data:
        for l_n in (add_coords(c, offset) for offset in offsets):
            n.add(l_n)

    return n

def step(data):
    new = set()
    all_neighbours = all_neighbour_coords(data)
    for coord in all_neighbours:
        n = neighbours(data, coord)
        if coord in data:
            if 1 < n < 4:
                new.add(coord)
        else:
            if n == 3:
                new.add(coord)
    
    return new

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        data = set()
        step_0_slice = file.read()
        for i, line in enumerate(step_0_slice.split("\n")):
            for j, c in enumerate(line): 
                if c == "#":
                    data.add((i, j, 0))

        print(len(data))
        for _ in range(6):
            data= step(data)
            print(len(data))

        print("final: ", len(data))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:        
        data = set()
        step_0_slice = file.read()
        for i, line in enumerate(step_0_slice.split("\n")):
            for j, c in enumerate(line): 
                if c == "#":
                    data.add((i, j, 0, 0))

        print(len(data))
        for _ in range(6):
            data= step(data)
            print(len(data))

        print("final: ", len(data))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)