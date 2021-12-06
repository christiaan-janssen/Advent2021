"""An implementation of playing bingo."""

from typing import List
import numpy as np


class Cell:
    """A cell represents on cell on a bingo card."""

    def __init__(self, number: int) -> None:
        """I will setup a single cell."""
        self.number = number
        self.marked = False

    def mark(self) -> None:
        """Mark this cell."""
        self.marked = True

    def is_marked(self) -> bool:
        """Check if this cell is marked."""
        return self.marked


class Line:
    """A line represents a row or column on a bingo card."""

    def __init__(self, numbers: List[int]):
        """I Setup a row or column on a bingo card."""
        self.cells = [Cell(i) for i in numbers]

    def mark_cell(self, number: int) -> None:
        """Mark the cell that matches the number."""
        for cell in self.cells:
            if cell.number == number:
                cell.mark()

    def check_line(self) -> bool:
        """Check this line to see if we won."""
        for cell in self.cells:
            if not cell.is_marked():
                return False

        return True


class Card:
    """A bingo card."""

    def __init__(self, numbers: str):
        """I Setup a gamecard."""
        self.cells = np.array([[Cell(int(i)) for i in j.split()]
                               for j in numbers.split('\n')])
        self.numbers = np.array([int(i) for i in numbers.split()[:-1]])
        self.marked = []

    def mark_cell(self, number: int):
        """Mark the number on the card."""
        for row in self.cells:
            for cell in row:
                if cell.number == number:
                    cell.mark()
                    self.marked.append(number)

    def _check_line(self, line: List[int]) -> bool:
        """Check this line to see if we won."""
        for cell in line:
            if not cell.is_marked():
                return False

        return True

    def print_column(self, data):
        l = []
        for c in data:
            l.append(c.number)
        return l

    def check_winner(self) -> bool:
        """Check to see if this card is a winner."""
        winner = False
        for row in self.cells:
            if self._check_line(row):
                print(f"Winning row: {self.print_column(row)}")
                winner = True

        for i in range(len(self.cells)):
            if self._check_line(self.cells[:, i]):
                print(
                    f"Winning column: {self.print_column( self.cells[:, i])}")

                winner = True

        return winner
