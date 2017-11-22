import json
import pandas as pd\
import sys
import time

tweets_data_path = sys.argv[1]

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line).lower()
        tweets_data.append(tweet)
        print(tweet['text'])
        print()
    except:
        continue

print("Total Msg:")
print(len(tweets_data))

for tw in tweets_data:
    disaster = False
    data = False
    month = False
    entertainment = False
    holiday = False
    action = False
    price = False
    time = False
    logistics = False
    sport = False
    location = False
    for w in tw:
        if w in kw.disaster:
            disaster = True
        if w in kw.data:
            data = True
        if w in kw.month:
            month = True
        if w in kw.entertainment:
            entertainment = True
        if w in kw.holiday:
            holiday = True
        if w in kw.action:
            action = True
        if w in kw.price:
            price = True
        if w in kw.time:
            time = True
        if w in kw.logistics:
            logistics = True
        if w in kw.sport:
            sport = True
        if w in kw.location:
            location = True

    