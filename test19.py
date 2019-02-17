from collections import defaultdict

text = 'hightemp.txt'

with open(text) as data:
    lines = data.readlines()

col_1 = [line.split('\t')[0] for line in lines]

pref = defaultdict(int)
for word in col_1:
    pref[word] += 1

result = sorted(pref.items(), key=lambda x: x[1], reverse=True)

for col in result:
    print('{i}({j})'.format(i = col[0], j = col[1]))