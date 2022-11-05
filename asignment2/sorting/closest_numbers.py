#https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    diff = []
    smallest = (arr[1]-arr[0])
    for x in range(1, n):
        if (arr[x] - arr[x-1]) <= smallest:
            smallest = (arr[x] - arr[x-1])
    for x in range(1, n):
        if (arr[x] - arr[x-1]) == smallest:
            diff += [arr[x-1], arr[x]]
    return diff
        
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
