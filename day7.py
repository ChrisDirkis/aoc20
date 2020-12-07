from itertools import *
from functools import *
from math import * 
import re

from typing import *

input_file = "inputs/day7"

def part_1():
    with open(input_file) as file:
        graph = dict()
        for line in file:
            name, children = re.match(r"(.*) bags contain (.*)$", line).groups()
            if (children == "no other bags."):
                continue
            csplit = children.split(", ")
            real_children = [" ".join(c.split(" ")[1:3]) for c in csplit]
            for child in real_children:
                if child in graph:
                    graph[child].append(name)
                else:
                    graph[child] = [name]
        print(graph)
        seen = set()
        working = ["shiny gold"]
        while len(working) > 0:
            item = working[0]
            working = working[1:]
            if item in seen:
                continue
            seen.add(item)

            if not item in graph:
                continue
            for parent in graph[item]:
                working.append(parent)

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



        print(get_bags("shiny gold", 1, graph) - 1)
        pass

def get_bags(bag, count, graph):
    if bag in graph:
        return count * (1 + sum(get_bags(child[1], child[0], graph) for child in graph[bag]))
    else:
        return count

if __name__ == "__main__":
    part_1()
    part_2()