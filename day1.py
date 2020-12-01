
def part_1():
    with open("inputs/day1") as file:
        numbers = [int(line) for line in file]
        for i, a in enumerate(numbers):
            b_numbers = (b for (j, b) in enumerate(numbers) if j > i)
            for b in b_numbers:
                if a + b == 2020:
                    print(a * b)
                    return

def part_2():
    with open("inputs/day1") as file:
        numbers = [int(line) for line in file]
        for i, a in enumerate(numbers):
            b_numbers = ((j, b) for (j, b) in enumerate(numbers) if j > i)
            for j, b in b_numbers:
                c_numbers = (c for (k, c) in enumerate(numbers) if k > j)
                for c in c_numbers:
                    if a + b + c == 2020:
                        print(a * b * c)
                        return


if __name__ == "__main__":
    part_1()
    part_2()