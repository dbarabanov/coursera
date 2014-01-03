template = 'PAWHEAE'
pattern = 'HEAGAWGHEE'

n, m = len(template), len(pattern)
cost = [[0]*m for _ in range(n)]
back_ptrs = [[None]*(m) for _ in range(n)]


def del_cost():
    return -2


def ins_cost():
    return -2


def sub_cost(i, j):
    if template[i] == pattern[j]:
        return 1
    return -2


i = n - 1
cost[i][m-1], back_ptrs[i][m-1] = sub_cost(i, m-1), pattern[m-1]
for j in range(m-2, -1, -1):
    cost[i][j], back_ptrs[i][j] = sub_cost(i, j), pattern[j]

j = m - 1
for i in range(n - 2, -1, -1):
    if template[i] == pattern[j]:
        cost[i][j], back_ptrs[i][j] = (del_cost() * (n-i-1)
                                       + sub_cost(i, j), pattern[j])
    else:
        cost[i][j], back_ptrs[i][j] = cost[i+1][j] + del_cost(), '-'

#print cost
#print back_ptrs

best_cost = None
for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        dc = del_cost() + cost[i+1][j]
        sc = sub_cost(i, j) + cost[i+1][j+1]
        if dc > sc:
            c, ptr = dc, '-'
        else:
            c, ptr = sc, pattern[j]
        ic = ins_cost() + cost[i][j+1]
        if ic > c:
            c, ptr = ic, 'i'
        cost[i][j], back_ptrs[i][j] = c, ptr

    if best_cost is None or cost[i][j] > best_cost:
        best_cost = cost[i][j]
        best_start = i
#    print cost
#    print back_ptrs
#    print '\n'.join([' '.join([str(back_ptrs[l][k]) for k in range(m)])
#                    for l in range(n)])
#    print '\n'.join(['\t'.join([str(cost[l][k]) for k in range(m)])
#                    for l in range(n)])

print best_cost, best_start
print '\n'.join([' '.join([back_ptrs[i][j] for j in range(m)])
                for i in range(n)])

top, bottom = [], []
i, j = best_start, 0
while True:
    if back_ptrs[i][j] == 'i':
        top.append('-')
        bottom.append(pattern[j])
        j += 1
    elif back_ptrs[i][j] == '-':
        top.append(template[i])
        bottom.append('-')
        i += 1
    else:
        top.append(template[i])
        bottom.append(pattern[j])
        i += 1
        j += 1
    if i >= n:
        break
print best_cost
print ''.join(top)
print ''.join(bottom)
