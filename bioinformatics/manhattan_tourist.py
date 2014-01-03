lines = """
4
4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2
"""
n, m = tuple([int(i) + 1 for i in lines.split('\n')[1:3]])
print n, m
m1 = [line for line in lines.split('-')[0].split('\n')[3:] if line]
m2 = [line for line in lines.split('-')[1].split('\n')[1:] if line]
down = [[int(i) for i in row.split(' ')] for row in m1]
right = [[int(i) for i in row.split(' ')] for row in m2]
print 'down: %s' % down
print 'right: %s' % right
cost = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(0)
    cost.append(row)
#print 'null cost: %s' % cost

for i in range(n - 1):
    cost[i+1][0] = down[i][0]
for j in range(m - 1):
    cost[0][j+1] = right[0][j]
#print 'cost with first: %s' % cost
for i in range(1, n):
    for j in range(1, m):
        cost[i][j] = max(cost[i-1][j]+down[i-1][j], cost[i][j-1]+right[i][j-1])
print 'cost: %s' % cost
print cost[n-1][m-1]
