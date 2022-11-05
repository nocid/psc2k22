#https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    a = 0
    s_correct = "SOS" * (len(s) // 3)
    for x in range(len(s)):
        if s[x] != s_correct[x]:
            a += 1
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
