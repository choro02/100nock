import math
text = 'hightemp.txt'

n = int(input('N >>> '))

with open(text) as data:
    lines = data.readlines()

count = len(lines)
unit = math.ceil(count / n)

for i, offset in enumerate(range(0, count, unit), 1):
    with open('child_{:02d}.txt'.format(i), mode='w') as output:
        for line in lines[offset:offset + unit]:
            output.write(line)