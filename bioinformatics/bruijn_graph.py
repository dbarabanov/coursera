from collections import defaultdict
k = 4
text = """
AAGATTCTCTAC
"""
print text
tuples = []
for i in range(1, len(text) - k):
    tuples.append((text[i: i+k-1], text[i+1: i+k]))
dd = defaultdict(set)
for t in tuples:
    dd[t[0]].add(t[1])
print '\n'.join(sorted([key + ' -> ' + ','.join([v for v in value])
                       for key, value in dd.items()]))
