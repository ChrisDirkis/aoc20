from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day16"
testing_file_name = data_file_name + "_test"

def is_valid(field, rule):
    a, b, c, d = rule
    return a <= field <= b or c <= field <= d

def is_ticket_invalid(ticket, rules):
    return any(not any(is_valid(field, rules[rule]) for rule in rules) for field in ticket)


def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        sections = file.read().split("\n\n")
        rule_groups = (re.match(r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)$", line).groups() for line in sections[0].split("\n"))
        rules = {name: (int(a), int(b), int(c), int(d)) for name, a, b, c, d in rule_groups}
        
        nearby = [[int(v) for v in line.split(",")] for line in sections[2].split("\n")[1:]]

        print(sum(sum(v for v in ticket if not any(is_valid(v, rules[rule]) for rule in rules)) for ticket in nearby))
                
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        sections = file.read().split("\n\n")
        rule_groups = (re.match(r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)$", line).groups() for line in sections[0].split("\n"))
        rules = {name: (int(a), int(b), int(c), int(d)) for name, a, b, c, d in rule_groups}
        print(rules)
        
        nearby = [[int(v) for v in line.split(",")] for line in sections[2].split("\n")[1:]]
        valid = [t for t in nearby if not is_ticket_invalid(t, rules)]

        candidates_per_field = [set(rules) for _ in valid[0]]
        for ticket in valid:
            for field, candidates in zip(ticket, candidates_per_field):
                invalid = []
                for candidate in candidates:
                    if not is_valid(field, rules[candidate]):
                        invalid.append(candidate)
                        #print(f"{field} invalidates {candidate}: {rules[candidate]}")
                for rule in invalid:
                    candidates.remove(rule)
        
        while any(len(candidates) > 1 for candidates in candidates_per_field):
            singles = [next(iter(candidates)) for candidates in candidates_per_field if len(candidates) == 1]
            for candidates in candidates_per_field:
                if len(candidates) > 1:
                    for single in singles:
                        candidates.discard(single)
        
        rules = [next(iter(c)) for c in candidates_per_field]
        my_ticket = [int(v) for v in sections[1].split("\n")[1].split(",")]
        print(prod(v for v, rule in zip(my_ticket, rules) if rule.startswith("departure")))

        
            

                
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)