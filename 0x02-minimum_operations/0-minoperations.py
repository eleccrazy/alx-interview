#!/usr/bin/env python3
"""
file: 0-minoperations.py
Desc: This python module contains code for alx-interview preparation
      algorithm.
Author: Gizachew Bayness
Date Created: Feb 9, 2023
"""


def minOperations(n) -> int:
    """A method to compute the min operations needed to result H characters"""
    if type(n) != int:
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count
