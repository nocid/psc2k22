#https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys



def plusMinus(arr):
    negative = 0
    positive = 0
    zero = 0
    for x in range(len(arr)):
        if arr[x] == 0:
            zero += 1
        elif arr[x] < 0:
            negative += 1
        elif arr[x] > 0:
            positive += 1
    print(format(positive/n,'.6f'))
    print(format(negative/n,'.6f'))
    print(format(zero/n,'.6f'))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
