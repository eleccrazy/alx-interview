#!/usr/bin/python3
"""
File: 0-lockboxes.py
Desc: This file contains a function which determines if all
      the boxes can be opened.
Author: Gizachew Bayness
Date Created: Jan 31, 2023
"""


def canUnlockAll(boxes):
    """A function that checks if all boxes can be opened"""
    keys = []  # List to store unique keys to unlock boxes
    length = len(boxes)
    idx = 0

    # Iterate over the boxes
    for i in boxes:
        # Iterate over numbers in each boxes
        for j in i:
            # Store unique numbers from boxes as keys
            if j not in keys and j != 0 and j != idx:
                keys.append(j)
        idx += 1
    # Sort the keys in ascending order
    keys = sorted(keys)
    # Iterate over the range of the length of the key, and make sure that each
    # box is opened by the keys.
    for k in range(1, length):
        if k != keys[k - 1]:
            return False
    return True
