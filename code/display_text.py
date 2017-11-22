import json
import pandas as pd
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
    disaster = 0
    data = 0
    month = 0
    entertainment = 0
    holiday = 0
    action = 0
    price = 0
    time = 0
    logistics = 0
    sport = 0
    location = 0
    for w in tw:
        if w in kw.disaster:
            disaster += 1
        if w in kw.data:
            data += 1
        if w in kw.month:
            month += 1
        if w in kw.entertainment:
            entertainment += 1
        if w in kw.holiday:
            holiday += 1
        if w in kw.action:
            action += 1
        if w in kw.price:
            price += 1
        if w in kw.time:
            time += 1
        if w in kw.logistics:
            logistics += 1
        if w in kw.sport:
            sport += 1
        if w in kw.location:
            location += 1

