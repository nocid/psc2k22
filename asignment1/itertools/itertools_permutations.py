#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations 
enter = input()
enter = enter.split(' ')
sortedl = sorted(enter[0])
sortedtoperm = ''.join(sortedl)
result = list(permutations(sortedtoperm, int(enter[1])))
for x in result:
    perm = ''.join(x)
    print(perm)