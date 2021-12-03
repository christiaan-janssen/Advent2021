"""Advent of Code 2021 Day 03."""

from typing import List
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


def count_most_common(line: List[str]) -> int:
    """Calculate the most common bit in a 'binary number'.
    :param line A list with the characters of the 'binary number'.
    :return: the most commen bit in the number.
    """
    zero, one = 0, 0
    for c in line:
        if int(c) == 0:
            zero += 1
        elif int(c) == 1:
            one += 1
    return 0 if zero > one else 1


def count_leaste_common(line: List[str]) -> int:
    """Calculate the leaste common bit in a 'binary number'.
    :param line A list with the characters of the 'binary number'.
    :return: the most commen bit in the number.
    """
    zero, one = 0, 0
    for c in line:
        if int(c) == 0:
            zero += 1
        elif int(c) == 1:
            one += 1
    return 0 if zero < one else 1


def calculate_oxygen_generator_rating(data):
    pos = 0
    while len(data) > 1:
        byte = '1'
        one = list(filter(lambda x: x[pos] == byte, data))

        byte = '0'
        zero = list(filter(lambda x: x[pos] == byte, data))

        if len(one) == len(zero):
            data = one
        elif len(one) > len(zero):
            data = one
        else:
            data = zero
        pos += 1

    return data[0]


def calculate_CO2_scrubber_rating(data):
    pos = 0
    while len(data) > 1:
        byte = '1'
        one = list(filter(lambda x: x[pos] == byte, data))

        byte = '0'
        zero = list(filter(lambda x: x[pos] == byte, data))

        if len(one) == len(zero):
            data = zero
        elif len(one) > len(zero):
            data = zero
        else:
            data = one
        pos += 1
    print(data)
    return data[0]


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
    data = get_input("day3.input", "\n")[:-1]

    oxygen = calculate_oxygen_generator_rating(data)
    co2 = calculate_CO2_scrubber_rating(data)

    return int(oxygen, 2) * int(co2, 2)


if __name__ == "__main__":
    print(f"Day 03 a: {puzzle_01()}")
    print(f"Day 03 b: {puzzle_02()}")
