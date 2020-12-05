from math import prod

def toboggan(slope, step):
    x, y = step
    width = len(slope[0]) - 1
    height = len(slope)
    return sum(slope[i][(x * i) % width] == "#" for i in range(0, height, y))

def part_1():
    with open("inputs/day3") as file:
        print(toboggan(file.readlines(), (3, 1)))

def part_2():
    with open("inputs/day3") as file:
        slope = file.readlines()
        steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        print(prod(toboggan(slope, step) for step in steps))

if __name__ == "__main__":
    part_1()
    part_2()