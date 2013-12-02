k = 3
t = 5
dna = """
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG
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


best_score, result = k, []
for i in range(len(dna[0]) - k + 1):
    best_motifs = [dna[0][i:i+k]]
    profile = form_profile_with_pseudocounts(best_motifs)
#    print 'initial profile: %s' % profile
    for t in range(1, len(dna)):
        kmer = find_best_kmer(dna[t], k, profile)
        best_motifs.append(kmer)
        profile = form_profile_with_pseudocounts(best_motifs)
    score = get_motifs_score(best_motifs)
    print 'best_motifs: %s, score: %s' % (best_motifs, score)
    if score < best_score:
        best_score, result = score, best_motifs
#print 'best score: %s' % best_score
print '\n'.join(result)
