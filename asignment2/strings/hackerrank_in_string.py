#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
        
def hackerrankInString(s):
    count = 0
    p = 'hackerrank'
    result = ''
    for x in p:
        while count < len(s):
            if x == s[count]:
                result += str(x)
                count += 1
                break
            else :
                count += 1
    if result == 'hackerrank':
        return 'YES'
    else : 
        return "NO"        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()