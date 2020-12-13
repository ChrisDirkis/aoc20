from itertools import *
from functools import *
from math import * 
import re

from typing import *

input_file = "inputs/day7"

def parse_line(line):
    parent, children_str = re.match(r"(.*) bags contain (.*)$", line).groups()
    if (children_str == "no other bags."):
        return (parent, [])
    
    children = [" ".join(c.split(" ")[1:3]) for c in children_str.split(", ")]
    return (parent, children)

def part_1():
    with open(input_file) as file:
        graph = dict()
        for line in file:
            name, children = parse_line(line)
            for child in children:
                if child in graph:
                    graph[child].append(name)
                else:
                    graph[child] = [name]

        seen = set()
        def search(item):
            if item in seen:
                return
            seen.add(item)
            if not item in graph:
                return
            for parent in graph[item]:
                search(parent)
        search("shiny gold")

        print(len(seen) - 1)
        pass

def part_2():
    with open(input_file) as file:
        graph = dict()
        for line in file:
            name, children = re.match(r"(.*) bags contain (.*)$", line).groups()
            if (children == "no other bags."):
                continue
            csplit = children.split(", ")
            real_children = [(int(c.split(" ")[0]), " ".join(c.split(" ")[1:3])) for c in csplit]
            for child in real_children:
                if name in graph:
                    graph[name].append(child)
                else:
                    graph[name] = [child]

        @cache
        def get_bags(bag, count):
            if bag in graph:
                return count * (1 + sum(get_bags(child[1], child[0]) for child in graph[bag]))
            else:
                return count

        print(get_bags("shiny gold", 1) - 1)
        pass



if __name__ == "__main__":
    part_1()
    part_2()