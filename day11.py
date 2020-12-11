from itertools import *
from functools import *
from math import * 
import re

from typing import *

data_file_name = "inputs/day11"
testing_file_name = data_file_name + "_test"

def worlds_equal(a, b):
    for i, a_line in enumerate(a):
        for j, a_elem in enumerate(a_line):
            if b[i][j] != a_elem:
                return False

    return True

def get_neighbours_1(world, i, j):
    points = product([i - 1, i, i + 1], [j - 1, j, j + 1])
    occupied = 0
    for x, y in points:
        if x < 0 or y < 0 or x >= len(world) or y >= len(world[0]) or (x == i and y == j):
            continue
        if world[x][y] == 1:
            occupied += 1
    return occupied

dirs = [(1, 0),(-1, 0),(1, 1),(-1, 1),(0, 1),(0, -1),(-1, -1),(1, -1)]
def get_neighbours_2(world, i, j):
    occupied = 0
    for dx, dy in dirs:
        x = i
        y = j
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= len(world) or y >= len(world[0]) or (x == i and y == j):
                break
            if world[x][y] == 1:
                occupied += 1
                break
            
            if world[x][y] == 0:
                break
    return occupied

def step(world, get_neighbours, leave_threshold):
    new_world = [list(l) for l in world]
    for i, line in enumerate(world):
        for j, elem in enumerate(line):
            n = get_neighbours(world, i, j) 
            if elem == 0:
                new_world[i][j] = 1 if n == 0 else 0
            elif elem == 1:
                new_world[i][j] = 0 if n >= leave_threshold else 1
    return new_world

def convert(line):
    a = line.replace("L", "0")
    b = a.replace("#", "1")
    c = b.replace(".", "2")
    return [int(x) for x in c]

def print_world(world):
    print("--")
    for line in world:
        print(line)

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        seats = [convert(l.strip()) for l in file]
        while True:
            new_seats = step(seats, get_neighbours_1, 4)
            #print_world(new_seats)
            if worlds_equal(seats, new_seats):
                break
            seats = new_seats
        print(sum(sum(e == 1 for e in line) for line in seats))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        seats = [convert(l.strip()) for l in file]
        while True:
            new_seats = step(seats, get_neighbours_2, 5)
            #print_world(new_seats)
            if worlds_equal(seats, new_seats):
                break
            seats = new_seats
        print(sum(sum(e == 1 for e in line) for line in seats))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)