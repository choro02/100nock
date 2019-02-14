text = 'hightemp.txt'


with open('col1.txt') as data1, \
        open('col2.txt') as data2, \
        open('col_merge.txt', mode='w') as data_m:
    c1 = data1.readlines()
    c2 = data2.readlines()
    c_m = [i.replace('\n', '')+ '\t' + j.replace('\n', '') for i, j in zip(c1, c2)]
    data_m.write('\n'.join(c_m) + '\n')

#print('\n'.join(c_m))