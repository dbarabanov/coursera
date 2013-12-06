from collections import defaultdict
kmers = """
GAGG
GGGG
GGGA
CAGG
AGGG
GGAG
""".split()
tuples = [(kmer[:len(kmer) - 1], kmer[1:]) for kmer in kmers]
dd = defaultdict(set)
for t in tuples:
    dd[t[0]].add(t[1])
print '\n'.join(sorted([key + ' -> ' + ','.join(sorted([v for v in value]))
                       for key, value in dd.items()]))
