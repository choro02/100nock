text = 'hightemp.txt'

n = int(input('N >>> '))


with open(text) as data:
    for i, line in enumerate(data):
        if i >= n:
            break
        print(line.rstrip())