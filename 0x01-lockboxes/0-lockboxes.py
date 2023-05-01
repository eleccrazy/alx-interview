#!/usr/bin/python3
"""
File: 0-lockboxes.py
Desc: This file contains a function which determines if all
      the boxes can be opened.
Author: Gizachew Bayness
Date Created: Jan 31, 2023
"""


def canUnlockAll(boxes):
    """A function that checks if all the boxes can be opened"""
    keys = []
    length = len(boxes)
    idx = 0

    for i in boxes:
        for j in i:
            if j not in keys and j != 0 and j != idx:
                keys.append(j)
        idx += 1
    keys = sorted(keys)
    for k in range(1, length):
        if k != keys[k - 1]:
            return False
    return True
