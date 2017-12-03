import json
from kw import features as kw_features
import numpy

if __name__ == '__main__':

  li_type = ['disaster','entertainment','holiday','sport']
  in_files = open('data/sport.txt', 'r').readlines()
  event_cluster = {}
  for tweet in in_files:
    id = tweet.split(',')[0]
    name = tweet.split(',')[1]
    date = tweet.split(',')[2]
    text = ' '.join(tweet.split(',')[3:])
    date_in_text = 0
    print(text)
    for w in text.split():
      if '/' in w:
        date_text = w.split('/')
        if len(date_text) == 2:
          MM = date_text[0]
          DD = date_text[1]
          if MM.isdigit() and DD.isdigit():
            date_in_text = int(MM)*100+int(DD)
            print(date_in_text)
            break
    if date_in_text == 0:
      continue
    if date_in_text not in event_cluster:
      event_cluster[date_in_text] = []
    event_cluster[date_in_text].append(tweet)

  for e in event_cluster:
    print('=========================', e, '=========================')
    for tw in event_cluster[e]:
      print(tw)
    