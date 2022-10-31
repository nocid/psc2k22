#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

from itertools import combinations_with_replacement
inp = input().split()
tobecomp = sorted(inp[0])
tobecompfinal = ''.join(tobecomp)
result = list(combinations_with_replacement(tobecompfinal, int(inp[1])))
for x in result:
    comb = ''.join(x)
    print(comb)