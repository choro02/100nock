sentence = 'I am an NLPer'

def ngram_w(sentence, n):
    w = sentence.split()
    li = []
    for i, m in enumerate(w):
        if i + n > len(w):
            return li
        li.append(w[i: i+n])

def ngram_s(sentence, n):
    li = []
    for i in range(len(sentence)):
        if i + n > len(sentence):
            return li
        li.append(sentence[i: i+n])


print('bi-gram in word')
print(ngram_w(sentence, 2))

print('bi-gram in char')
print(ngram_s(sentence, 2))