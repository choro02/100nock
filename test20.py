import gzip
import json

file = 'jawiki-country.json.gz'

with gzip.open(file, 'rt') as data:
    for line in data:
        data_json = json.loads(line)
        if data_json['title'] == 'イギリス':
            print(data_json['text'])
            break
