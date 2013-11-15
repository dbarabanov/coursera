import itertools
from collections import defaultdict

nucs = ['A', 'C', 'T', 'G']
text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
nucs_product = [i for i in itertools.product(nucs, repeat=d)]
idx_combinations = [i for i in itertools.combinations(range(k), d)]


def apply_nucs(kmer, positions, nucs):
    kmer = list(kmer)
    assert len(positions) == len(nucs)
    for i, pos in enumerate(positions):
        kmer[pos] = nucs[i]
    return ''.join(kmer)


def fuzzy_kmers(kmer, nucs_product, idx_combinations):
    kmers = set()
    for t in idx_combinations:
        for n in nucs_product:
            kmers.add(apply_nucs(kmer, t, n))
    return kmers

dd = defaultdict(int)
for i in range(len(text)-k):
    kmer = text[i:i+k]
    for x in fuzzy_kmers(kmer, nucs_product, idx_combinations):
        dd[x] += 1

max_dd = max(dd.values())
print ' '.join(sorted([key for key, v in dd.items() if v == max_dd]))
