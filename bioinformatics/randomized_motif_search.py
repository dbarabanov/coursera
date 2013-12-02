import random
k = 8
t = 5
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


def find_best_kmer(text, k, profile):
    best_kmer, best_prob = text[:k], 0
    for i in range(len(text) - k + 1):
        kmer = text[i: i+k]
        prob = get_prob(kmer, profile)
        if prob > best_prob:
            best_kmer, best_prob = kmer, prob
    return best_kmer


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
for t in range(1000):
    motifs = []
    for i in range(len(dna)):
        random.seed()
        r = random.randint(0, len(dna[0]) - k)
        motifs.append(dna[i][r: r+k])
    best_motifs = motifs
    best_score = get_motifs_score(best_motifs)
#    print """initial motifs: %s, global_best_score: %s\
#iteration: %s global_best_motifs:\n%s"""\
# % (motifs, global_best_score, t, '\n'.join(global_best_motifs))
#    while True:
    for x in range(10000):
        profile = form_profile_with_pseudocounts(motifs)
        motifs = [find_best_kmer(dn, k, profile) for dn in dna]
        score = get_motifs_score(motifs)
        if score < best_score:
            best_score, best_motifs = score, motifs
        else:
#            print 'breaking at %s with motifs: %s, score: %s'\
#                  % (x, motifs, score)
            break
    if best_score < global_best_score:
        global_best_score, global_best_motifs = best_score, best_motifs
        print 'improoving global_best_motifs: %s, global_best_score: %s'\
              % (global_best_motifs, global_best_score)

print 'global best score: %s' % global_best_score
print '\n'.join(global_best_motifs)
