#https://www.hackerrank.com/challenges/countingsort2/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    a = [0]
    frqarr = a * 100
    sortedarr = []
    for x in range(0, n):
        i = int(arr[x])
        frqarr[i] += 1
    for value in range(0, len(frqarr)):
        if frqarr[value] == 0:
            continue
        if frqarr[value] != 0:
            while frqarr[value] != 0:
                sortedarr.append(value)
                frqarr[value] -= 1
    return sortedarr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()