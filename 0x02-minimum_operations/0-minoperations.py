#!/usr/bin/python3
"""
file: 0-minoperations.py
Desc: This python module contains code for alx-interview preparation
      algorithm.
Author: Gizachew Bayness
Date Created: Feb 9, 2023
"""


def minOperations(n: int) -> int:
    """A method to compute the min operations needed to result H characters"""
    if type(n) != int or n < 2:
        return 0
    repr = 1
    ops = 0
    status = False
    while repr < n:
        if n % repr == 0 and not status:
            copy = repr
            ops += 1
            status = True
        else:
            repr += copy
            ops += 1
            status = False
    return ops
