from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day19"
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        sections = file.read().split("\n\n")
        rules = dict((int(r), v) for r, v in (re.match(r"^(\d+): (.*)$", line).groups() for line in sections[0].split("\n")))
        for key in rules:
            rules[key] = [[int(v) if v[0] != '"' else v[1] for v in s.strip().split(" ")] for s in rules[key].split("|")]

        def match(val, key, offset, depth = 0):
            for subrule in rules[key]:
                suboffset = offset

                for node in subrule:
                    if isinstance(node, int):
                        suboffset = match(val, node, suboffset, depth + 1)
                        if (suboffset == -1):
                            break
                    else: 
                        if val[suboffset] == node:
                            suboffset += 1
                        else:
                            suboffset = -1
                            break

                if suboffset != -1:
                    return suboffset
                    
            return -1
        
        
        print(sum(match(val, 0, 0) == len(val) for val in sections[1].split("\n")))

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:        
        sections = file.read().split("\n\n")
        rules = dict((int(r), v) for r, v in (re.match(r"^(\d+): (.*)$", line).groups() for line in sections[0].split("\n")))
        for key in rules:
            rules[key] = [[int(v) if v[0] != '"' else v[1] for v in s.strip().split(" ")] for s in rules[key].split("|")]

        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]
        
        def match(val, rule, offsets):
            if len(offsets) == 0:
                return offsets
            if len(rule) == 1:
                if isinstance(rule[0], int):
                    subrules = rules[rule[0]]
                    suboffsets = []
                    for subrule in subrules:
                        suboffsets += match(val, subrule, offsets)
                    return list(set(suboffsets))
                else:
                    return [offset + 1 for offset in offsets if offset < len(val) and val[offset] == rule[0]]
            else:
                for step in rule:
                    offsets = match(val, [step], offsets)
                
                return offsets
        
        print(sum(any(o == len(val) for o in match(val, rules[0][0], [0])) for val in sections[1].split("\n")))

if __name__ == "__main__":
    #part_1(testing_file_name)
    #part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)