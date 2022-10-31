Msize = int(input())
M=set([int(x) for x in input().split()])
Nsize = int(input() )
N=set([int(x) for x in input().split()])

symdif = M.difference(N)
symdif1 = N.difference(M)
symdifu = symdif.union(symdif1)
symdif = sorted(symdifu)

for x in symdif:
    print(x)
   