#!/usr/bin/python3
"""
file: 0-pascal_triangle.py
Desc: This module contains code for implementing the pascal's
      triangle of n rows.
Author: Gizachew Bayness
Date Created: Jan 26, 2023
"""


def pascal_triangle(n):
    """This function returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    pascal = []
    if n <= 0:
        return pascal

    for i in range(n):
        inner = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner.append(1)
                continue
            top_inner = pascal[i - 1]
            value = top_inner[j - 1] + top_inner[j]
            inner.append(value)

        pascal.append(inner)

    return pascal
