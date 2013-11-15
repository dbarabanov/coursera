pattern = 'ATTCTGGA'
text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
d = 3
results = []
for i in range(len(text)-len(pattern)+1):
    if [text[i:i+len(pattern)][j] == l for j, l in enumerate(pattern)].count(True) >= len(pattern) - d:
        results.append(i)
print ' '.join([str(r) for r in results])
#with open('appr_pattern_matching_results.txt', 'w') as f:
#    f.write(' '.join([str(r) for r in results]))
