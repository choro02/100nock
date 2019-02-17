import gzip
import json
import re
import urllib.parse, urllib.request
import requests
import pprint

file = 'jawiki-country.json.gz'

def article_UK():

    with gzip.open(file, 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return (data_json['text'])
                
def remove_markup(target):
    reg = re.compile(r'''
        (\'{2,5})
        (.*?)
        (\1)
        ''', re.MULTILINE + re.VERBOSE)

    target = reg.sub(r'\2', target)
    
    
    reg = re.compile(r'''
        \[\[
        (?:
            [^|]*?
            \|
        )*?
        ([^|]*?)
        \]\]
        ''', re.MULTILINE + re.VERBOSE)

    target = reg.sub(r'\1', target)
    
    reg = re.compile(r'''
        \{\{lang
        (?:
            [^|]*?
            \|
        )*?
        ([^|]*?)
        \}\}
        ''', re.MULTILINE + re.VERBOSE)

    target = reg.sub(r'\1', target)

    reg = re.compile(r'''
        \[http:\/\/
        (?:
            [^\s]*?
            \s
        )?
        ([^]]*?)
        \]
        ''', re.MULTILINE + re.VERBOSE)

    target = reg.sub(r'\1', target)

    reg = re.compile(r'''
        <
        \/?
        [br|ref]
        [^>]*?
        >
        ''', re.MULTILINE + re.VERBOSE)

    target = reg.sub('', target)

    return target



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
for field in fields:
    result[field[0]] = remove_markup(field[1])

fname_flag = result['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(fname_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

#print(url)

r = requests.get(url)
url_flag = r.json()['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url_flag)
