#https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    left_right = 0
    right_left = 0
    for j in range(n):
        for i in range(n):
            if i == j:
                left_right += arr[j][i]
            if i + j == n-1:
                right_left += arr[j][i]
    result = abs(left_right-right_left)
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()