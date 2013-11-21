rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'


def rna_codon_map():
    codon_map = {}
    with open('codon_table.txt') as f:
        for line in f:
            pair = line.strip().split()
            if len(pair) == 2:
                codon_map[pair[0]] = pair[1]
            else:
                codon_map[pair[0]] = ''
    return codon_map


print ''.join([rna_codon_map()[rna[i:i+3]] for i in range(0, len(rna), 3)])
