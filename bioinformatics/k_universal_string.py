import itertools
from collections import defaultdict
k = 4
kmers = [''.join(p) for p in itertools.product(['0', '1'], repeat=k)]
print kmers
input = [kmer[:-1] + ' -> ' + kmer[1:] for kmer in kmers]
print input
#input = """
#CTT -> TTA
#ACC -> CCA
#TAC -> ACC
#GGC -> GCT
#GCT -> CTT
#TTA -> TAC
#""".split('\n')
#with open('/Users/dbarabanov/Downloads/dataset_57_6.txt') as f:
#    input = [s.strip() for s in f.readlines()]
#with open('string_reconstruction_input.txt') as f:
    #input = [s.strip() for s in f.readlines()]
edges = [tuple(edge.split(' -> ')) for edge in input if edge]
print edges
edges = [(t[0], [i for i in t[1].split(',')]) for t in edges]
print 'edges 2: %s ' % edges
#graph = {x: y for x, y in edges}
graph = defaultdict(list)
for x, y in edges:
    graph[x] += y
print 'graph: %s' % graph
start = graph.keys()[0]
degrees = defaultdict(int)
for k in graph:
    for v in graph[k]:
        degrees[k] += 1
        degrees[v] += 1
print 'degrees: %s' % degrees

#assert False
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
        if current != next and current in graph:
            cycle.append(next)
        current = next
        print 'cycles: %s' % cycles
        print graph


def traverse(tree, root):
    out = []
    for r in tree[root]:
        if r != root and r in tree:
            out += traverse(tree, r)
        else:
            out.append(r)
    return out

#print '->'.join([str(i) for i in traverse(cycles, start)])
cycle = traverse(cycles, cycles.keys()[0])
print cycle
print ''.join([s[0] for s in cycle[:-2]]) + cycle[-1][:-1]
