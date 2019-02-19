import json, config
from requests_oauthlib import OAuth1Session

CK = config.Consumer_key
CS = config.Consumer_secret
AT = config.Access_token
ATS = config.Access_secret
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

params ={'count' : 5}
req = twitter.get(url, params = params)

if req.status_code == 200:
    timeline = json.loads(req.text)
    for tweet in timeline:
        print(tweet['user']['name']+'::'+tweet['text'])
        print(tweet['created_at'])
        print('----------------------------------------------------')
else:
    print("ERROR: %d" % req.status_code)