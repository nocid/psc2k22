#https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for x in range(1, len(arr)):
        for a in range(0, x):
            if arr[x] < arr[a]:
                item = arr.pop(x)
                arr.insert(a, item)
        print(' '.join(map(str, arr)))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
