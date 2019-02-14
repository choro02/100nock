string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nation Might Also Sign Peace Security Clause. Arther King Can.'
w = string.split(' ')
print(w)
t = (1,5,6,7,8,9,15,16,19)

dic = {
    (x[0:2] if i+1 not in t else x[0:1])
    :i+1
    for i, x
    in enumerate(w)
}

print(dic)