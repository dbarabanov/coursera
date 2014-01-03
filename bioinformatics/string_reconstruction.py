from collections import defaultdict
input = """
CTT -> TTA
ACC -> CCA
TAC -> ACC
GGC -> GCT
GCT -> CTT
TTA -> TAC
""".split('\n')
#with open('/Users/dbarabanov/Downloads/dataset_57_6.txt') as f:
#    input = [s.strip() for s in f.readlines()]
#with open('string_reconstruction_input.txt') as f:
    #input = [s.strip() for s in f.readlines()]
edges = [tuple(edge.split(' -> ')) for edge in input if edge]
edges = [(t[0], [i for i in t[1].split(',')]) for t in edges]
graph = {x: y for x, y in edges}
#print graph
degrees = defaultdict(int)
for k in graph:
    for v in graph[k]:
        degrees[k] += 1
        degrees[v] -= 1
source = [k for k, v in degrees.items() if v == 1][0]
sinc = [k for k, v in degrees.items() if v == -1][0]
start = graph.keys()[0]
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

cycle = traverse(cycles, start)
for i in range(1, len(cycle)):
    if cycle[i-1] == sinc and cycle[i] == source:
        boarder = i
path = cycle[boarder:]+cycle[1:boarder]
print ''.join([s[0] for s in path]) + path[-1][1:]
