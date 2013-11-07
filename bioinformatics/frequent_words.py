from collections import defaultdict
dd = defaultdict(int)
text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
for i in range(len(text)-k):
    dd[text[i:i+k]] += 1
print ' '.join(sorted([key for key, v in dd.items() if v == max(dd.values())]))
#CATG GCAT
