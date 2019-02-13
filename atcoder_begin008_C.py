import math
import itertools

n = int(input())
numer = 0

c = []
for i in range(n):
  c.append(int(input()))

t = tuple(c)

li = list(itertools.permutations(t))

#print(li)

for k in li:
    d = [[k[i], True] for i in range(n)]
    #print(d, 'default')


    for i in range(n-1):
        for j in range(n-1-i):
            if d[i+j+1][0] % d[i][0] == 0:
                d[i+j+1][1] = not d[i+j+1][1]
            else:
                pass
    #print(d)

    numer += len([x for x in d if x[1]])

    #print(numer)


denom = math.factorial(n) 

print(numer/denom)
