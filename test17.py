text = 'hightemp.txt'

with open(text) as data:
    lines = data.readlines()
    tmp = [i.split('\t') for i in lines]
    line_1 = [i[0] for i in tmp]

    set_1 = set(line_1)
    sorted_line = list(set_1)
    sorted(sorted_line)

for n in sorted_line:
    print(n)