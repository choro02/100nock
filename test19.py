from itertools import groupby

text = 'hightemp.txt'

with open(text) as data:
    lines = data.readlines()

col_1 = [line.split('\t')[0] for line in lines]

pref = {}
for word in col_1:
    pref[word] = pref.get(word, 0) + 1

result = sorted(pref.items(), key=lambda x: x[1], reverse=True)

for col in result:
    print('{i}({j})'.format(i = col[0], j = col[1]))