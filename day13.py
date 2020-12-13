from itertools import *
from functools import *
from math import * 
import re

from typing import *

data_file_name = "inputs/day13"
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = file.readlines()
        earliest = int(lines[0])
        busses = [int(v) for v in lines[1].split(",") if v != "x"]
        best_departures = [(b, ceil(earliest / b) * b) for b in busses]
        offset = [(id, best - earliest) for id, best in best_departures]
        s_offset = sorted(offset, key=lambda x: x[1])
        print(s_offset[0][0] * s_offset[0][1])
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = file.readlines()
        busses = [(i, int(v)) for i, v in enumerate(lines[1].split(",")) if v != "x"]
        t = 1
        step = 1
        for i in range(len(busses)):
            to_consider = busses[:i + 1]

            while True:
                if all((t + i) % v == 0 for i, v in to_consider):
                    p = prod(v for _, v in to_consider)
                    step = p
                    print(f"step is now {p}")
                    break

                t += step

        print(t)
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)