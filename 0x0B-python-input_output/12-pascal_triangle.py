#!/usr/bin/python3
"""A pascal traingle function."""


def pascal_triangle(n):
    """A function  that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    List = []
    if (n <= 0):
        return []

    for i in range(n):
        row = [1]

        for j in range(1, i):
            row.append(List[i - 1][j - 1] + List[i - 1][j])

        if i > 0:
            row.append(1)

        List.append(row)

    return List
