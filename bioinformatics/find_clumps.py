from collections import defaultdict
text = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k, l, t = 5, 50, 4

kmers = defaultdict(list)
for i in range(len(text) - k):
    kmers[text[i:i+k]].append(i)

results = []
for kmer, positions in kmers.items():
    for i, pos in enumerate(positions[t-1:]):
        if pos - positions[i-t] <= l:
            results.append(kmer)
            break
print ' '.join(results)
