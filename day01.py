"""Advent of Code 2021 Day 01."""

from utils.tools import get_input


def puzzle_01():
    """Calculate the sonar depth increase."""
    data = get_input("day1.input", "\n")
    data = [int(val) for val in data[:-1]]
    count = 0
    for i, var in enumerate(data):
        if not i+1 > len(data)-1:
            if var < data[i+1]:
                count += 1

    return count


def puzzle_02():
    """Calculate the sonar depth increase."""
    input = get_input("day1.input", "\n")
    count = 0
    data = [int(val) for val in input[:-1]]
    for i, var in enumerate(data):
        if not i+3 > len(data)-1:
            a = sum(data[i:i+3])
            b = sum(data[i+1:i+4])
            if a < b:
                count += 1

    return count

if __name__ == "__main__":
    print(f"Day 01 a: {puzzle_01()}")
    print(f"Day 01 b: {puzzle_02()}")
