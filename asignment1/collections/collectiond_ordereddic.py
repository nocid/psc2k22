from collections import OrderedDict
numitems = int(input())
orddic = {}
orddic = OrderedDict()
for a in range(numitems):
    items = input().split()
    price = int(items[-1])
    key = ' '.join(map(str, items[0:-1]))
    if key in orddic:
        orddic[key] += price
    else:
        orddic[key] = price
for word in orddic:
    print(word, orddic[word])     
