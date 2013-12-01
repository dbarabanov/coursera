import itertools
k = 3
d = 1
dna = """
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT
"""
regions = dna.split()
#print regions
kmers = [''.join(p) for p in itertools.product(list('ACTG'), repeat=k)]
#print kmers
results = []


def get_mutants(kmer, d):
    def apply_nucs(kmer, positions, nucs):
        kmer = list(kmer)
        assert len(positions) == len(nucs)
        for i, pos in enumerate(positions):
            kmer[pos] = nucs[i]
        return ''.join(kmer)
    nucs_product = [i for i in itertools.product(list('ACTG'), repeat=d)]
    idx_combinations = [i for i in itertools.combinations(range(k), d)]
    return [apply_nucs(kmer, positions, nucs)
            for positions in idx_combinations
            for nucs in nucs_product]

mutants = dict((kmer, get_mutants(kmer, d)) for kmer in kmers)

for kmer in kmers:
    present_in_all_regions = True
    for region in regions:
        kmer_present = False
        for mutant in mutants[kmer]:
            if mutant in region:
#                print '%s in %s: %s' % (kmer, region, mutant in region)
                kmer_present = True
                break
        if not kmer_present:
            present_in_all_regions = False
            break
    if present_in_all_regions:
        results.append(kmer)
print ' '.join(sorted(results))
