import random

sample_string = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

def shuffle_word(x):
    if len(x) <= 4:
        return x
    else:
        li = [i for i in x[1:-1]]
        random.shuffle(li)
        word = x[0] + ''.join(li) + x[-1]
        #print(word)
        return word

a = sample_string.split(' ')
b = [shuffle_word(x) for x in a]

print(sample_string)
print(' '.join(b))