dna = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
peptide = 'MA'


def dna_codon_map():
    codon_map = {}
    with open('codon_table.txt') as f:
        for line in f:
            pair = line.strip().split()
            pair[0] = pair[0].replace('U', 'T')
            if len(pair) == 2:
                codon_map[pair[0]] = pair[1]
            else:
                codon_map[pair[0]] = 'X'
    return codon_map


def reverse_complement(text):
    return "".join(reversed([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[l]
                   for l in list(text)]))
results = []
for f in range(3):
    translated = ''.join([dna_codon_map()[dna[i:i+3]]
                          for i in range(f, ((len(dna)-f)/3)*3, 3)])
    for i in range(len(translated) - len(peptide) + 1):
        if translated[i:i+len(peptide)] == peptide:
            results.append(dna[i*3+f:i*3+f+3*len(peptide)])

for f in range(3):
    translated = ''.join([dna_codon_map()[reverse_complement(dna)[i:i+3]]
                          for i in range(f, ((len(dna)-f)/3)*3, 3)])
    for i in range(len(translated) - len(peptide) + 1):
        if translated[i:i+len(peptide)] == peptide:
            results.append(reverse_complement(
                reverse_complement(dna)[i*3+f:i*3+f+3*len(peptide)]))

print '\n'.join(results)
