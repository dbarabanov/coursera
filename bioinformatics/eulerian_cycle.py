input = """
0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6
"""
edges = [tuple(edge.split(' -> ')) for edge in input.split('\n') if edge]
edges = [(int(t[0]), [int(i) for i in t[1].split(',')]) for t in edges]
graph = {x: y for x, y in edges}

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

print '->'.join([str(i) for i in traverse(cycles, 0)])
