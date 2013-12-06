patterns = [s for s in"""
ATGCG
GCATG
CATGC
AGGCA
GGCAT
""".split() if s]

for i1, p1 in enumerate(patterns):
    for i2, p2 in enumerate(patterns):
        if p1[1:] == p2[:len(p2) - 1] and i1 != i2:
            print p1 + ' -> ' + p2
