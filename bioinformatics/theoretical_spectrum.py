input = 'LEQN'
masses = {}
with open('integer_mass_table.txt') as f:
    for line in f:
        pair = line.strip().split()
        masses[pair[0]] = int(pair[1])
#print masses


def get_mass(peptide):
    return sum([masses[p] for p in peptide])


def subpeptide(peptide, pos, length):
    if pos+length <= len(peptide):
        return peptide[pos: pos+length]
    else:
        return peptide[pos:] + peptide[:length + pos - len(peptide)]

combos = [subpeptide(input, p, l) for p in range(len(input))
          for l in range(1, len(input))]

print ' '.join([str(j) for j in
                sorted([get_mass(i) for i in combos] + [0, get_mass(input)])])
