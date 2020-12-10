from itertools import *
from functools import *
from math import * 
import re

from typing import *

data_file_name = "inputs/day10"
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        joltages = sorted(int(l) for l in file)
        joltages.insert(0, 0)
        offset_j = joltages[1:]
        offset_j.append(joltages[-1]+3)
        pairs = zip(joltages, offset_j)
        diffs = [p[1] - p[0] for p in pairs]
        print(sum(d == 1 for d in diffs) * sum(d == 3 for d in diffs))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        joltages = [int(l) for l in file]
        joltages.insert(0, 0)
        joltages.append(max(joltages)+3)
        graph = dict()
        for j in joltages:
            graph[j] = set(_j for _j in joltages if _j > j and _j <= j + 3)

        @cache
        def get_path_count(a, b):
            if a == b:
                return 1
            routes = graph[a]
            return sum(get_path_count(v, b) for v in routes)

        print(get_path_count(0, joltages[-1]))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)