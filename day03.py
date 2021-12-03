"""Advent of Code 2021 Day 03."""

from utils.tools import get_input


test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".split("\n")

def count_most_common(line):
    zero, one = 0, 0
    for c in line:
        if int(c) == 0:
            zero += 1 
        elif int(c) == 1:
            one += 1
    return 0 if zero > one else 1

def count_leaste_common(line):
    zero, one = 0, 0
    for c in line:
        if int(c) == 0:
            zero += 1 
        elif int(c) == 1:
            one += 1
    return 0 if zero < one else 1

def puzzle_01():
    data = get_input("day3.input", "\n")
    gamma, epsilon = "", ""
    numbers = [[] for i in range(len(data[0]))]

    for _, line in enumerate(data):
        for j, c in enumerate(line):
            numbers[j] += c

    for line in numbers:
        gamma += str(count_most_common(line))

    for line in numbers:
        epsilon += str(count_leaste_common(line))

    return int(gamma, 2) * int(epsilon, 2)


def puzzle_02():
    data = get_input("day03.input", " ")
    print(data)

if __name__ == "__main__":
    print(f"Day 03 a: {puzzle_01()}")
    #print(f"Day 03 b: {puzzle_02()}")
    
