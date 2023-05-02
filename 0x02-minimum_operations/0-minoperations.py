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
    if type(n) != int or n < 1:
        return 0
    ch = 'H'
    ops = 0
    status = False
    while True:
        if n % len(ch) == 0 and not status:
            copy = ch
            ops += 1
            status = True
        else:
            ch += copy
            ops += 1
            status = False
        if len(ch) == n:
            break

    return ops
