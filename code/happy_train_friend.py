import json
import numpy as np
import sys
import time
from kw import features as kw_features
from nltk.corpus import stopwords

if __name__ == '__main__':
    stopWords = set(stopwords.words('english'))
    
    with open('dictionary', 'r',encoding='utf-8', errors='ignore') as f:
        content = f.readlines()
    f.close()
    wordlist = []
    for l in content:
        w, _ = l.split()
        wordlist.append(w)

    tweets_data_paths = ["1103_compress.json", "1104_compress.json", "1105_compress.json", "1107_compress.json"]
    # tweets_data_paths = ["1103_compress.json","1104_compress.json","1105_compress.json",\
    # "1106_compress.json","1107_compress.json","1108_compress.json","1109_compress.json",\
    # "1110_compress.json","1112_compress.json","1113_compress.json","1114_compress.json",\
    # "1115_compress.json","1116_compress.json","1117_compress.json","1118_compress.json",\
    # "1119_compress.json","1120_compress.json","1121_compress.json","1127_compress.json",\
    # "1128_compress.json"]
    docs = []
    for path in tweets_data_paths:
        print(path)
        tweets_file = open('data/'+path, 'r',encoding='utf-8', errors='ignore')
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tw_d = tweet
                tw = tweet['text'].lower()
                doc_vec = [0]*len(wordlist)
                doc = tw.split()
                #print(doc)
                for w in doc:
                    w = w.strip('’…,.;:?!\r\b\t\'\",()[]{}|-=+*_ \n')
                    if w in stopWords:
                        continue
                    if w in wordlist:
                        doc_vec[wordlist.index(w)] = 1
                docs.append(doc_vec)                        
                #print(sum(doc_vec))
            except:
                    continue
    arr = np.array(docs)
    print(arr)
    np.save("data/doc_vec", arr)
        
        
