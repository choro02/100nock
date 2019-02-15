from itertools import groupby

text = 'hightemp.txt'

with open(text) as data:
    lines = data.readlines()

col_1 = [line.split('\t')[0] for line in lines]

col_1.sort()
result = [(col_1, len(list(group))) for col_1, group in groupby(col_1)]

result.sort(key=lambda col_1: col_1[1], reverse=True)


for col in result:
    print('{i}({j})'.format(i = col[0], j = col[1]))