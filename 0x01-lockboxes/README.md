## Lockboxes
### Requirements
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: ```def canUnlockAll(boxes)```
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box ```boxes[0]``` is unlocked
- Return ```True``` if all boxes can be opened, else return ```False```


#### Test File: main.py
```
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False

boxes = [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [
    6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6]]
print(canUnlockAll(boxes))  # True

boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [
    7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5], ]
print(canUnlockAll(boxes))  # False
```
### Explanation
##### The method returns ```True``` for the first input in the above test file. Let's deep dive into it.
- The first box ```boxes[0]``` is unlocked as per the instruction and it contains 1 to open the second box in ```boxes```.
- The second box which is numbered as 1 is unlocked by the key found in the first box.
- The second box also contains 2 as a key to unlock the third box in ```boxes```. The third box also contains 3 as a key to unlock the fourth box.
- The fourth box contains 4 as a key to unlock the fifth box.
- Summary: Boxes are numbered from 0 to n-1. This indicates that ```[[1] -> 0, [2] -> 1, [3] -> 2, [4] -> 3, [] -> 4]```. Based on the boxes number, a key from the first box opens the second box, a key from the second opens the third, and soon...

##### The method returns ```True``` for the second input in the above test file.
- The first box contains 1, 4, and 6 as a key to open the second, fifth, and seventh boxes in the ```boxes```. Note, boxes are numbered from 0 to n-1
- The second box contains 2 as a key to open the third box.
- The third box contains 0, 4, and 1 as a key to open boxes. Here, 0 can be ignored because the first box is always opened as stated in the question. Also, the second and the fifth boxes are already opened by the keys from the first box.
- The fourth box contains 5, 6, and 2 as a key to open the the 6th, 7th, and 3rd boxes.
- The fifth box contains 3 as a key to open the 4th box.
- At this stage, all boxes are opened from the keys found in the previous boxes. So, the function returns ```True```

##### Let's see the case for the third input for the above test file.  ```False```
- Everything works as the previous test input except that the forth box numbered as 3 can't be opened by the key found from itself.
- The fourth box numbered as 3 has a key 3. No other boxes have 3 as a key to open the fourth box.

##### The method for the last test input also returns  ```Falsse```
- There is no a key to open the second box. No other boxes have 1 as a key to open the second box. The only box that contains 1 as a key is the second box itself.
- Note: A box can't be opened by the key found from itself.
