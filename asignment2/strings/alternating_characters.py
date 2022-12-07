#https://www.hackerrank.com/challenges/alternating-characters/problem

"""
import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    counter = 0
    for x in range(1, len(s)):
        if s[x] == s[x-1]:
            counter += 1
    return counter
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()"""
            
n = int(input())
permu = ''.join(input().split())
permu = list(map(int, permu))
print(permu)
minx = min(permu)
maxx = max(permu)
incr = [minx]
decr = []
for x in range(n):
    if permu[x] == minx:
        posmin = x
    if permu[x] == maxx:
        posmax = x
print(posmax)
#increasing subsequence
for x in range(posmin, n-1):
   # if pos == n or pos == n-1:
        #if permu[pos] > permu[]
    if x == posmin:
        pos = posmin
    if x != posmin:
        mini = min(permu[(pos+1): n])
        for i in range(n):
            if permu[i] == mini:
                pos = i 
        incr.append(permu[pos])
#print(incr)

for x in range(n-1,posmax , -1):
    if x == posmax:
        pos = posmax
    if x != posmax:
        maxi = max(permu[(pos+1): n])
        for i in range(n):
            if permu[i] == maxi:
                pos = i 
        decr.append(permu[pos])
print(*decr)