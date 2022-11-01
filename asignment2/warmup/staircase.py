#https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen



import math
import os
import random
import re
import sys



def staircase(n):
    for x in range(1, n+1):
        print((n-x)*' ' + x*'#')
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
