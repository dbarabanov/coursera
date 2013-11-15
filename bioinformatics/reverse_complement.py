text = 'AAAACCCGGT'
complement_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
print "".join(reversed([complement_map[l] for l in list(text)]))
