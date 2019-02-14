text = 'hightemp.txt'

n = int(input('N >>> '))

if n > 0:
    with open(text) as data:
        lines = data.readlines()[-n:]

    for i in lines:
        print(i.rstrip())