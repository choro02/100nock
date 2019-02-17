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
                

reg = re.compile(r'''^(.*\[\[Category.*\]\].*)$''', re.MULTILINE + re.VERBOSE)

result = reg.findall(article_UK())

for line in result:
    print(line)