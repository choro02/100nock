text = 'hightemp.txt'

with open(text) as data:
   s = data.readlines()
   t = [i.split('\t') for i in s]

c1 = [i[0] for i in t]
c2 = [i[1] for i in t]

with open('col1.txt', mode='w') as data:
    data.write('\n'.join(c1) + '\n')

with open('col2.txt', mode='w') as data:
    data.write('\n'.join(c2) + '\n')

print('\n'.join(c1))
print('\n'.join(c2))