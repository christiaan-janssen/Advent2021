"""Advent of Code 2021 Day 02."""

from typing import Tuple
from utils.tools import get_input

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split('\n')


def parse_input(line: str) -> Tuple:
    """Convert a direction to a set of coords. 

    :param line is a direction like `down 5`. 
    :return: a Tuple with an x an y coordinate.
    """
    x, y = 0, 0

    orders = line.split(' ')
    if orders[0] == 'down':
        y = -int(orders[-1])
    elif orders[0] == 'up':
        y = int(orders[-1])
    elif orders[0] == 'forward':
        x = int(orders[-1])

    return (x, y)


def puzzle_01() -> int:
    data = get_input("day2.input", "\n")
    total_x, total_y = 0, 0
    for line in data:
        x, y = parse_input(line)
        total_x += x
        total_y += y

    return abs(total_x * total_y)


def puzzle_02():
    data = get_input("day2.input", "\n")
    total_x, total_y, aim = 0,0,0

    for line in data:
        x, y = parse_input(line)
        total_x += x
        aim += y
        total_y += aim * x

    return abs(total_x * total_y)


if __name__ == "__main__":
    print(f"Day 02 a: {puzzle_01()}")
    print(f"Day 02 b: {puzzle_02()}")
