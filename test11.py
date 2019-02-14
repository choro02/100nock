text = 'hightemp.txt'

with open(text) as data:
    for i in data:
        print(i.replace('\t', ' '))