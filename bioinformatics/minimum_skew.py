text = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
cum = 0
min = 0
results = [0]
for i, l in enumerate(text):
    if l == 'G':
        cum += 1
    elif l == 'C':
        cum -= 1
    if cum < min:
        min = cum
        results = [i]
    elif cum == min:
        results.append(i)
print ' '.join([str(r+1) for r in results])
