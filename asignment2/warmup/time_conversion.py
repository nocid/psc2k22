#https://www.hackerrank.com/challenges/time-conversion/problem



import math
import os
import random
import re
import sys



def timeConversion(s):
    heure = s[0:2]
    minutes = s[3:5]
    secondes = s[6:8]
    x = s[8:]
    if x == "AM" and heure == "12":
        heure = "00"
    if x == "PM" and int(heure) < 12:
        heure = str(int(heure)+12)
    return "{}:{}:{}".format(heure,minutes,secondes)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
