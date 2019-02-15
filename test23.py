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
                

reg = re.compile(r'''
    ^(={2,})\s*(.+?)\s*\1.*$
    ''', re.MULTILINE + re.VERBOSE)

result = reg.findall(article_UK())

for line in result:
    level = len(line[0]) - 1
    print('{indent}{section}({level})'
    .format(indent='\t' * (level - 1), section=line[1], level=level))
        