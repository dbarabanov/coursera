money = 40
money = 19154
coins = [int(s) for s in """
50,25,20,10,5,1
""".split(',')]
coins = [int(s) for s in """
32,12,81,21,5,3,1
""".split(',')]
#print coins
cash = [0]
for i in range(1, money+1):
    cash.append(min([cash[i - c] for c in coins if i >= c]) + 1)
#    print cash
print cash[money]
