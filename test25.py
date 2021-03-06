import gzip
import json
import re

file = 'jawiki-country.json.gz'

def article_UK():

    with gzip.open(file, 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return (data_json['text'])
                

reg1 = re.compile(r'''
    ^\{\{
    基礎情報.*?$(.*?)
    \}\}$
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

contents = reg1.findall(article_UK())

reg2 = re.compile(r'''
    ^\|
    (.*?)
    \s*
    =
    \s*
    (.*?)
    (?:
        (?=\n\|)
        | (?=\n$)
    )
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = reg2.findall(contents[0])

result = {}
keys_test = []
for field in fields:
    result[field[0]] = field[1]
    keys_test.append(field[0])

for item in sorted(result.items(),
        key=lambda field: keys_test.index(field[0])):
    print(item)