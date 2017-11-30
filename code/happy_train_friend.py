import json
import pandas as pd
import sys
import time
from kw import features as kw_features
from nltk.corpus import stopwords

if __name__ == '__main__':
    stopWords = set(stopwords.words('english'))
    
    with open('dictionary', 'r') as f:
        content = f.readlines()
    f.close()
    wordlist = []
    for l in content:
        w, _ = l.split()
        wordlist.append(w)
    print(wordlist)
    #tweets_data_paths = ["1103_compress.json", "1104_compress.json", "1105_compress.json", "1107_compress.json"]
    tweets_data_paths = ["1103_compress.json"]
    
    docs = []
    with open('doc_vec', 'w') as f:
    
        for path in tweets_data_paths:
            tweets_file = open('../data/'+path, "r")
            for line in tweets_file:
                try:
                    tweet = json.loads(line)
                    tw_d = tweet
                    tw = tweet['text'].lower()
                    doc_vec = [0]*len(wordlist)
                    doc = tw.split()
                    print(doc)
                    for w in doc:
                        w = w.strip('…,.;:?!\r\b\t\'\",()[]{}|-=+*_ \n')
                        if w in stopWords:
                            continue
                        if w in wordlist:
                            doc_vec[wordlist.index(w)] = 1
                    #print(doc_vec)
                    #docs.append(doc_vec)                        
                    print(sum(doc_vec))
                    f.write(','.join(doc_vec)+'\n')
                except:
                        continue
            