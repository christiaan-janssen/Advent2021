"""Advent of Code 2021 Day 07."""

from typing import List
from utils.tools import get_input

test_input = """16,1,2,0,4,2,7,1,2,14""".split()


def move_to(crab: int, position: int) -> int:
    """Return the cost to move a crab to a position."""
    return abs(position - crab)

def move_more_fuel(crab: int, position:int) -> int:
    pass

def align_crabs(crab_positions: List[int]):
    """Align the crab positions, using as less feul as possble."""
    least_fuel_cost = None
    for position in range(crab_positions[-1]):
        fuel_cost = sum([move_to(crab, position) for crab in crab_positions])
        if least_fuel_cost is None:
            least_fuel_cost = fuel_cost
        elif fuel_cost < least_fuel_cost:
            least_fuel_cost = fuel_cost

    return least_fuel_cost


def puzzle_01():
    """Puzzle 01 day 7."""
    data = get_input("day7.input", " ")
    # data = test_input
    data = [int(i) for i in data[0].split(',')]
    data.sort()
    return align_crabs(data)


def puzzle_02():
    data = get_input("day07.input", " ")
    print(data)


if __name__ == "__main__":
    print(f"Day 07 a: {puzzle_01()}")
    # puzzle_02()
