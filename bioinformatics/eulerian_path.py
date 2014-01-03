from collections import defaultdict
input = """
0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6
""".split('\n')
with open('/Users/dbarabanov/Downloads/dataset_57_5 (3).txt') as f:
    input = f.readlines()
#with open('eulerian_path.txt') as f:
    #input = f.readlines()
edges = [tuple(edge.split(' -> ')) for edge in input if edge]
edges = [(int(t[0]), [int(i) for i in t[1].split(',')]) for t in edges]
graph = {x: y for x, y in edges}
degrees = defaultdict(int)
for k in graph:
    for v in graph[k]:
        degrees[k] += 1
        degrees[v] -= 1
source = [k for k, v in degrees.items() if v == 1][0]
sinc = [k for k, v in degrees.items() if v == -1][0]
#print 'source: %s, sinc: %s' % (source, sinc)

if sinc in graph.keys():
    graph[sinc].append(source)
else:
    graph[sinc] = [source]

cycles = {}
while graph:
    current = graph.iterkeys().next()
    cycle = [current]
    cycles[current] = cycle
    while current in graph:
        next = graph[current][0]
        del graph[current][0]
        if len(graph[current]) == 0:
            del graph[current]
        current = next
        cycle.append(next)


def traverse(tree, root):
    out = []
    for r in tree[root]:
        if r != root and r in tree:
            out += traverse(tree, r)
        else:
            out.append(r)
    return out

cycle = traverse(cycles, 0)
for i in range(1, len(cycle)):
    if cycle[i-1] == sinc and cycle[i] == source:
        boarder = i
path = cycle[boarder:]+cycle[1:boarder]
print '->'.join([str(i) for i in path])
