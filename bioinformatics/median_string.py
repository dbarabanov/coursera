import itertools
k = 3
dna = """
AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTACGGGACAG
"""

regions = dna.strip().split()
#print regions
kmers = [''.join(p) for p in itertools.product(list('ACTG'), repeat=k)]


def get_sum_distance(pattern, regions):
    return sum([min_hamming_distance(pattern, region) for region in regions])


def hamming_distance(str1, str2):
    return sum(itertools.imap(str.__ne__, str1, str2))


def min_hamming_distance(pattern, text):
    return min([hamming_distance(pattern, text[i: i+len(pattern)])
                for i in range(len(text) - len(pattern) + 1)])

best_kmer = kmers[0]
best_score = get_sum_distance(best_kmer, regions)
for kmer in kmers:
    score = get_sum_distance(kmer, regions)
    if score < best_score:
        best_kmer, best_score = kmer, score
print best_kmer
