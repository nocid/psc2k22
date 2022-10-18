#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

from itertools import combinations
inp = input().split(' ')
tobecomb = sorted(inp[0])
tobecombf = ''.join(tobecomb)
counter = 1
for x in range(int(inp[1])):
    result = list(combinations(tobecombf, counter))
    counter += 1
    for x in result:
        perm = ''.join(x)
        print(perm)