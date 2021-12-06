"""Advent of Code 2021 Day 04."""

from utils.tools import get_input
from utils.bingo import Card
import numpy as np

test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n\n")


def puzzle_01():
    data = get_input("day4.input", "\n\n")
    # data = test_data
    numbers = [int(i) for i in data[0].split(",")]
    data = data[1:]
    cards = []

    for line in data:
        cards.append(Card(line))

    for number in numbers:
        for card in cards:
            card.mark_cell(number)
            if card.check_winner():
                return np.setdiff1d(card.numbers, np.array(card.marked)).sum() * number


# def puzzle_02():
#     data = get_input("day04.input", " ")
#     print(data)


if __name__ == "__main__":
    print(f"Day 04 a: {puzzle_01()}")
    # print(f"Day 04 b: {puzzle_02()}")
