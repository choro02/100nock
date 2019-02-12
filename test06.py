def ngram(sentence, n):
    li = []
    for i in range(len(sentence)):
        if i + n > len(sentence):
            return li
        li.append(sentence[i: i+n])

set_x = set(ngram('paraparaparadise',2))
print('X ' + str(set_x))

set_y = set(ngram('paragraph',2))
print('Y ' + str(set_y))

set_or = set_x | set_y
print(str(set_or))

set_and = set_x & set_y
print(str(set_and))

set_sub = set_x - set_y
print(str(set_sub))

print(str('se' in set_x))
print(str('se' in set_y))