## Minimum Operations
### Requirements
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: ```def minOperations(n)```
- Returns an integer
- If ```n``` is impossible to achieve, return ```0```
- Example:
```
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```


#### Test File: main.py
```
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 21
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 19170307
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 972
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 0
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = -12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 2147483640
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```
### Output for the above test cases
```
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
Min # of operations to reach 9 char: 6
Min # of operations to reach 21 char: 10
Min # of operations to reach 19170307 char: 47613
Min # of operations to reach 972 char: 19
Min # of operations to reach 1 char: 0
Min # of operations to reach 0 char: 0
Min # of operations to reach -12 char: 0
Min # of operations to reach 2147483640 char: 326
```
