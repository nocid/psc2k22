#https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value = arr[n-1]
    for x in range(n-2, -1, -1):
        if arr[x] > value:
            arr[x+1] = arr[x]
            print(' '.join(map(str, arr)))
        else:
            arr[x+1] = value
            print(' '.join(map(str, arr)))
            break
        if x == 0:
            arr[x] = value
            print(' '.join(map(str, arr)))
            break

if __name__ == '__main__':
    n = int(input().strip())


    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)