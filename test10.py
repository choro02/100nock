text = 'hightemp.txt'

with open(text) as data:
    count = sum(1 for i in data)

print(count)