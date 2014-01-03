template = 'GTAGGCTTAAGGTTA'
pattern = 'TAGATA'

n, m = len(template), len(pattern)
cost = [[0]*(m + 1) for _ in range(n + 1)]
back_ptrs = [[None]*(m) for _ in range(n)]


def del_cost():
    return -1


def ins_cost():
    return -1


def sub_cost(i, j):
    if template[i] == pattern[j]:
        return 1
    return -1


for j in range(m):
    cost[n][j] = ins_cost() * (m - j)

best_cost = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
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

    if j == 0 and cost[i][j] >= best_cost:
        best_cost = cost[i][j]
        best_start = i
#    print cost
#    print back_ptrs
#print best_cost, best_start
#print '\n'.join([' '.join([back_ptrs[i][j] for j in range(m)])
#                for i in range(n)])

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
    if j >= m:
        break
print best_cost
print ''.join(top)
print ''.join(bottom)
