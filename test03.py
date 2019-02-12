import re
str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
w = str.split(' ')
li = [re.match('[a-zA-z]',x).group() for x in w]
#m = re.match('[a-zA-Z]',str).group()
print(w)
print(li)