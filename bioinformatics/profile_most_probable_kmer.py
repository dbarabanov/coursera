text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
k = 5
#A C G T
profile = """
0.2 0.4 0.3 0.1
0.2 0.3 0.3 0.2
0.3 0.1 0.5 0.1
0.2 0.5 0.2 0.1
0.3 0.1 0.4 0.2
"""
profile = [[float(f) for f in s.split()] for s in profile.split('\n') if s]
positions = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def get_prob(kmer, profile):
    return reduce(lambda x, y: x * y,
                  [profile[j][positions[c]]
                   for j, c in enumerate(list(kmer))])

best_kmer, best_prob = text[:k], 0
for i in range(len(text) - k + 1):
    kmer = text[i: i+k]
    prob = get_prob(kmer, profile)
    if prob > best_prob:
        best_kmer, best_prob = kmer, prob
#    print '%s: %s' % (kmer, prob)
print best_prob
print best_kmer
