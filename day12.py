from itertools import *
from functools import *
from math import * 
import re

from typing import *

data_file_name = "inputs/day12"
testing_file_name = data_file_name + "_test"

def rotate(dir, angle):
    angle = -angle / 180 * 3.141592563589793
    c, s = (int(round(cos(angle))), int(round(sin(angle))))
    dir = [dir[0] * c - dir[1] * s, dir[0] * s + dir[1] * c]
    return dir
    

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        pos = [0, 0]
        dir = [1, 0]
        for line in file:
            inst = line[0]
            val = int(line[1:])
            if inst == "F":
                pos[0] += dir[0] * val
                pos[1] += dir[1] * val
            elif inst == "R":
                dir = rotate(dir, val)
            elif inst == "L":
                dir = rotate(dir, -val)
            elif inst == "N":
                pos[1] += val
            elif inst == "E":
                pos[0] += val
            elif inst == "S":
                pos[1] -= val
            elif inst == "W":
                pos[0] -= val
        print(abs(pos[0]) + abs(pos[1]))


        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        pos = [0, 0]
        way = [10, 1]
        dir = [1, 0]
        for line in file:
            inst = line[0]
            val = int(line[1:])
            if inst == "F":
                pos[0] += way[0] * val
                pos[1] += way[1] * val
            elif inst == "R":
                way = rotate(way, val)
            elif inst == "L":
                way = rotate(way, -val)
            elif inst == "N":
                way[1] += val
            elif inst == "E":
                way[0] += val
            elif inst == "S":
                way[1] -= val
            elif inst == "W":
                way[0] -= val
        print(abs(pos[0]) + abs(pos[1]))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)