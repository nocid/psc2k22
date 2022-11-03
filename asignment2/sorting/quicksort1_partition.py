#https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    pivot = arr[0]
    left = []
    equal = [pivot]
    right = []
    for x in range(1, len(arr)):
        if arr[x] == pivot:
            equal.append(arr[x])
        if arr[x] < pivot:
            left.append(arr[x])
        if arr[x] > pivot:
            right.append(arr[x])
    arr = left + equal + right
    return arr  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
