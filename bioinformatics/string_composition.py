k = 5
text = 'CAATCCAAC'
print '\n'.join(sorted([text[i:i+k] for i in range(len(text) - k + 1)]))
