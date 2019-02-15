text = 'hightemp.txt'

with open(text) as data:
    lines = data.readlines()

lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

for line in lines:
    print(line, end='')
