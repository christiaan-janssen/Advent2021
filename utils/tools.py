"""Reusable functions for the project."""

import os

def get_input(day: str, split_on='') -> str:
    """Return the puzzle input based on the day provided as a string."""
    f = open(f'input/{day}', 'r')
    data = f.read()
    f.close()

    if (split_on != ''):
        data = data.split(split_on)

    return data
