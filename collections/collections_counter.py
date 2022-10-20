#https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter
numshoes = int(input())
shoesizes = input().split(' ')
shoesizes = list(map(int, shoesizes))
countersize = Counter(shoesizes)
numcustom = int(input())
salary = 0
for x in range(numcustom):
    demande = input().split(' ')
    demande = list(map(int, demande))
    if demande[0] in countersize.keys():
        if countersize[demande[0]] != 0:
            countersize[demande[0]] -= 1
            salary += demande[1]
        else:
            pass
    else:
        pass
print(salary)

