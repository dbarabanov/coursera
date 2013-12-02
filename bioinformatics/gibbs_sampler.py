import random
k = 8
t = 5
n = 100
dna = """
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA
"""
dna = [s for s in dna.split() if s]
positions = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def get_prob(kmer, profile):
    return reduce(lambda x, y: x * y,
                  [profile[j][positions[c]]
                   for j, c in enumerate(list(kmer))])


def find_gibbs_kmer(text, k, profile):
    probs = [get_prob(text[i: i+k], profile) for i in range(len(text) - k + 1)]
    r = random.random() * sum(probs)
    for i, p in enumerate(probs):
        r -= p
        if r < 0:
            idx = i
            break
    return text[idx: idx+k]


def form_profile_with_pseudocounts(kmers):
    profile = [[0, 0, 0, 0] for i in range(len(kmers[0]))]
#    print 'profile: %s kmers: %s' % (profile, kmers)
    for kmer in kmers:
        for i, c in enumerate(kmer):
            profile[i][positions[c]] += 1
    for i, freqs in enumerate(profile):
        for f in range(len(freqs)):
            profile[i][f] += 1
            profile[i][f] /= 2 * float(len(kmers))
    return profile


def get_motifs_score(motifs):
    return len(motifs[0]) -\
        sum([max(p) for p in form_profile_with_pseudocounts(motifs)])

motifs = []
for i in range(len(dna)):
    random.seed()
    r = random.randint(0, len(dna[0]) - k)
    motifs.append(dna[i][r: r+k])

global_best_motifs = motifs
global_best_score = get_motifs_score(global_best_motifs)

for y in range(20):
    print 'iter: %s' % y
    motifs = []
    for i in range(len(dna)):
        random.seed()
        r = random.randint(0, len(dna[0]) - k)
        motifs.append(dna[i][r: r+k])
    best_motifs = motifs
    best_score = get_motifs_score(best_motifs)
#    print 'initial best score: %s' % (best_score)

    for x in range(n):
        random.seed()
        r = random.randint(0, t - 1)
        profile = form_profile_with_pseudocounts(motifs[:r] + motifs[r+1:])
#    print 'dna: %s, r: %s' % (dna, r)
        motif = find_gibbs_kmer(dna[r], k, profile)
        motifs[r] = motif
        score = get_motifs_score(motifs)
        if score < best_score:
            best_score, best_motifs = score, motifs
#        print 'iter: %s, score: %s, best score: %s' % (x, score, best_score)
    if best_score < global_best_score:
        global_best_score, global_best_motifs = best_score, best_motifs
        print 'improoving global_best_motifs:\n%s,\nglobal_best_score: %s'\
              % ('\n'.join(global_best_motifs), global_best_score)

print 'global best score: %s' % global_best_score
print '\n'.join(global_best_motifs)
expected_motifs = [s for s in """
TCTCGGGG
CCAAGGTG
TACAGGCG
TTCAGGTG
TCCACGTG
""".split() if s]
expected_motifs = [s for s in """
TAGACATTCGGACGT
CAGCGCCATGGAGCC
CAGAAGTATGGAGCC
CATGGACATGGAGCC
CAGACACATGGTAGC
CAGACACATGCCCCC
TTGTCACACGCAGCA
CAGACCTCTGGAGCC
CAGACACATGGACAT
CAGCTGCATGGAGCC
CAGACATTCGGAGCC
CTGAGGCCCAAACCA
CAGACACAGCTAGCC
CAGACAGCGGGAGCC
CAGACACATAACGCC
CTCCCACATGGAGCC
CAGACGACTGGAGCC
CAGAGGAATGGAGCC
CAGACACCCCGAGCC
TCGACACATGGAGCA
""".split() if s]
expected_score = get_motifs_score(expected_motifs)
#print 'expected_score: %s' % expected_score
