#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
num = int(input())
resume = namedtuple('resume', ','.join(input().split()))
sum_marks = sum([int(resume(*(input().split())).MARKS) for _ in range(num) ])
sumall = round((sum_marks/num),2)
print(sumall)