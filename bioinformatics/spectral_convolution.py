input = '0 137 186 323'
spectrum = sorted([int(i) for i in input.split()])
result = []
for i, v in enumerate(spectrum):
    for s in spectrum[:i]:
        if v != s:
            result.append(v-s)
result.sort()
print ' '.join([str(r) for r in result])
