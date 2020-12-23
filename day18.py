from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day18"
testing_file_name = data_file_name + "_test"

def subexpr_1(expr, start, stop):
    val = expr[start]
    oper = ""
    for i in range(start + 1, stop):
        token = expr[i]
        if (start - i) % 2 == 1:
            oper = token
        else: 
            if oper == "+":
                val += token
            else:
                val *= token
    return val

def subexpr_2(expr, start, stop):
    i = 0
    my_expr = list(expr[start:stop])
    print(my_expr)
    while i < len(my_expr):
        token = my_expr[i]
        if token == "+":
            l = my_expr[i - 1]
            r = my_expr[i + 1]
            my_expr[i - 1] = l + r
            del my_expr[i:i+2]
            i -= 1
        i += 1
            
    p = prod(token for token in my_expr if token != "*")
    return p

def calc_expression(expr, subexpr_parser):
    opens = []
    i = 0
    while i < len(expr):
        token = expr[i]
        if token == "(":
            opens.append(i)
        elif token == ")":
            start = opens[-1]
            stop = i
            flat = subexpr_parser(expr, start + 1, stop)
            del expr[start:stop]
            expr[start] = flat

            del opens[-1]
            i -= (stop - start)

        i += 1
    return subexpr_parser(expr, 0, len(expr))

valid_tokens = {"(", ")", "+", "*"}

def tokenise(line):
    expr = []
    for val in line:
        if "0" <= val <= "9":
            expr.append(int(val))
        elif val in valid_tokens:
            expr.append(val)
    return expr


def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        expressions = [tokenise(line) for line in file.readlines()]
        print(sum(calc_expression(expr, subexpr_1) for expr in expressions))

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        expressions = [tokenise(line) for line in file.readlines()]
        print(sum(calc_expression(expr, subexpr_2) for expr in expressions))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)