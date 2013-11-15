import itertools
from collections import defaultdict

text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1

nucs = ['A', 'C', 'T', 'G']
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


def rev_comp(pattern):
    complement_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(reversed([complement_map[l] for l in list(pattern)]))

dd = defaultdict(int)
for i in range(len(text)-k):
    kmer = text[i:i+k]
    for x in fuzzy_kmers(kmer, nucs_product, idx_combinations):
        dd[x] += 1
    for x in fuzzy_kmers(rev_comp(kmer), nucs_product, idx_combinations):
        dd[x] += 1

max_dd = max(dd.values())
print ' '.join(sorted([key for key, v in dd.items() if v == max_dd]))
