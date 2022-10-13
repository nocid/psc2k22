from itertools import product

A = input().split(' ')
A = [eval(i) for i in A]
B = input().split(' ')
B = [eval(i) for i in B]

product = list(product(A, B))

for i in product:
    print(i, end=' ')