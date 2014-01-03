template = 'PLEASANTLY'
pattern = 'MEANLY'

n, m = len(template), len(pattern)
cost = [[0]*m for _ in range(n)]


def del_cost(i, j):
    return 1


def ins_cost(i, j):
    return 1


def sub_cost(i, j):
    if template[i-1] == pattern[j-1]:
        return 0
    return 1


for i in range(1, n):
    cost[i][0] += cost[i-1][0] + ins_cost(i, 0)

for j in range(1, m):
    cost[0][j] += cost[0][j-1] + ins_cost(0, j)


for i in range(1, n):
    for j in range(1, m):
        cost[i][j] = min(cost[i-1][j-1] + sub_cost(i, j),
                         cost[i-1][j] + ins_cost(i, j),
                         cost[i][j-1] + del_cost(i, j))
print cost[n-1][m-1]
