import re

def cipher (string):
    reg = '[a-z]'
    tmp = [chr(219 - ord(x)) if re.match(reg, x) else x for x in string]
    #print(tmp)

    result = ''
    for c in tmp:
        result += str(c)
    
    return result

string = input('文字列を入力　＞＞＞　')

a = cipher(string)
print(a)

b = cipher(a)
print(b)

if b != string:
    print('復元失敗')