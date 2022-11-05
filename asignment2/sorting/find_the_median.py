#https://www.hackerrank.com/challenges/find-the-median/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    arr.sort()
    median = int(n/2)
    for x in range(0, n):
        if x == median:
            return arr[x]
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()