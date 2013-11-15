pattern = 'ATAT'
text = 'GATATATGCATATACTT'
print ' '.join([str(i) for i in range(len(text)-len(pattern)) if text[i:i+len(pattern)] == pattern])
