import re
str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nation Might Also Sign Peace Security Clause. Arther King Can.'
w = str.split(' ')
li = [re.match('[a-zA-z]',x).group() for x in w]
#m = re.match('[a-zA-Z]',str).group()
print(w)
print(li)