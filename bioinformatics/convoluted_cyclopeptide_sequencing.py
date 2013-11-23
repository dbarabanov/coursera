from collections import defaultdict
m = 20
n = 60
input = '57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'
spectrum = sorted([int(i) for i in input.split()])

convolution = []
for i, v in enumerate(spectrum):
    for s in spectrum[:i]:
        if v != s:
            convolution.append(v-s)
convolution.sort()
print 'convolution: %s' % convolution
filtered = [c for c in convolution if c >= 57 and c <= 200]
#print 'filtered: %s' % filtered
elements = sorted([(c, filtered.count(c)) for c in set(filtered)],
                  key=lambda tup: tup[1], reverse=True)
#print 'elements(%s): %s' % (len(elements), elements)
leaders = [e for e in elements if e[1] >= elements[m][1]]
#print 'leaders(%s): %s' % (len(leaders), leaders)
alphabet = sorted([l[0] for l in leaders])
print 'alphabet (%s): %s' % (len(alphabet), alphabet)


def cyclopeptide(peptide):
    def subpeptide(peptide, pos, length):
        if pos+length <= len(peptide):
            return peptide[pos: pos+length]
        else:
            return peptide[pos:] + peptide[:length + pos - len(peptide)]
    return [subpeptide(peptide, p, l) for p in range(len(peptide))
            for l in range(1, len(peptide) + 1)]


def cyclospectrum(peptide):
    return sorted([sum(p) for p in cyclopeptide(peptide)] + [0])


def expand_list(peptides, masses):
    if len(peptides) == 0:
        return [[m] for m in masses]
    return [p + [m] for p in peptides for m in masses]


def score(peptide, spectrum_map):
    peptide_map = defaultdict(int)
    for p in peptide:
        peptide_map[p] += 1
    return sum([min(peptide_map[k], spectrum_map[k])
               for k in peptide_map.keys()])


def cut(peptides, spectrum_map, n):
    scores = sorted([(p, score(cyclospectrum(p), spectrum_map))
                    for p in peptides],
                    key=lambda tup: tup[1], reverse=True)
    leaders = [s for s in scores if n >= len(scores) or s[1] >= scores[n][1]]
    return [leader[0] for leader in leaders]


spectrum_map = defaultdict(int)
for i in spectrum:
    spectrum_map[i] += 1

leaders = []
best = (0, 0)
for i in range(50):
    expanded = expand_list(leaders, alphabet)
    print 'i=%s. len(expanded): %s' % (i, len(expanded))
    leaders = cut([p for p in expanded], spectrum_map, n)
    top_score = score(cyclospectrum(leaders[0]), spectrum_map)
    if top_score > best[1]:
        best = (leaders[0], top_score)
    print 'best(%s): %s' % (best[1], '-'.join(str(i) for i in best[0]))
    leaders = [p for p in leaders if sum(p) <= max(spectrum)]
    print 'len(cut): %s' % len(leaders)
    if len(leaders) == 0:
        break
