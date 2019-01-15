#!/bin/python3
"""
https://www.hackerrank.com/challenges/alternating-characters/problem
"""


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == "A" and s[i+1] =="A" or s[i] == "B" and s[i+1] == "B":
            cnt += 1
    return cnt
