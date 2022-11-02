#https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true

import math
import os
import random
import re
import sys



def aVeryBigSum(ar):
    total = 0
    for x in ar:
        total += x
    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
