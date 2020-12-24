from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day24"
testing_file_name = data_file_name + "_test"

def move(coord, step):
    x, y = coord
    if step == "e":
        return (x + 1, y)
    elif step == "w":
        return (x - 1, y)
    elif step == "ne":
        return (x if y % 2 == 0 else x + 1, y + 1)
    elif step == "nw":
        return (x - 1 if y % 2 == 0 else x, y + 1)
    elif step == "se":
        return (x if y % 2 == 0 else x + 1, y - 1)
    elif step == "sw":
        return (x - 1 if y % 2 == 0 else x, y - 1)

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [re.findall(r"(nw|ne|sw|se|w|e)", line) for line in file]
        black = set()
        for line in lines:
            point = (0, 0)
            for step in line:
                point = move(point, step)
            if point in black:
                black.remove(point)
            else:
                black.add(point)

        print(len(black))
        pass


all_moves = ["e", "w", "ne", "nw", "se", "sw"]
def adjacent(coord): 
    return [move(coord, step) for step in all_moves]

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [re.findall(r"(nw|ne|sw|se|w|e)", line) for line in file]
        black = set()
        for line in lines:
            point = (0, 0)
            for step in line:
                point = move(point, step)
            if point in black:
                black.remove(point)
            else:
                black.add(point)
        
        for _ in range(100):
            new_black = set()
            to_check = list(set(list(black) + sum((adjacent(t) for t in black), [])))
            for tile in to_check:
                adj = sum(t in black for t in adjacent(tile))
                if tile in black and not (adj == 0 or adj > 2):
                    new_black.add(tile)
                elif tile not in black and adj == 2:
                    new_black.add(tile)
            black = new_black

        print(len(black))

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)