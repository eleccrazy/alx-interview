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
    canUnlockAll = False
    keys = {0: True}
    n_boxes = len(boxes)
    while(True):

        n_keys = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
