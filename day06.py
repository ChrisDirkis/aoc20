from itertools import *
from functools import *
from math import * 
import re

from typing import *

input_file = "inputs/day6"

def part_1():
    with open(input_file) as file:
        groups = ["".join(g.split("\n")) for g in file.read().split("\n\n")]
        print(sum(len(set(iter(group))) for group in groups))

d = list("qwertyuiopasdfghjklzxcvbnm")
def part_2():
    with open(input_file) as file:
        groups = file.read().split("\n\n")

        answersum = 0
        for group in groups:
            answers = dict()
            for c in d:
                answers[c] = 0
            for line in group.split("\n"):
                for char in line.strip():
                    answers[char] += 1
            answersum += sum(answers[c] == len(group.split("\n")) for c in d)

        print(answersum)
            
        pass

if __name__ == "__main__":
    part_1()
    part_2()