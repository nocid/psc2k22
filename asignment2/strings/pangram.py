#https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true

import math
import os
import random
import re
import sys
import string
string.ascii_lowercase

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alf = list(string.ascii_lowercase)
    counter = 0
    i = 0
    for x in range(len(alf)):
        if alf[x-i] in map(str.lower, s):
            alf.remove(alf[x-i])
            counter += 1
            i += 1
        else:
            continue
    if counter == 26:
        return 'pangram'
    if counter != 26:
        return 'not pangram'
             
   
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
