import json
from nltk.corpus import stopwords
import re
import operator
from stoplist import stop_ls 

if __name__ == '__main__':

    tweets_data_paths = ["1103_compress.json", "1104_compress.json", "1105_compress.json", "1107_compress.json"]
    stopset = set(stop_ls)
    stopWords = set(stopwords.words('english'))
    for path in tweets_data_paths:
        tweets_file = open('../data/'+path, "r")
        total_msg = 0
        vectors = []
        dic = {}
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tw_d = tweet
                tw = tweet['text'].lower()
                for w in tw.split():
                    w = w.strip('…,.;:?!\r\b\t\'\",()[]{}|-=+*_ \n')
                    if w in stopWords:
                        continue
                    if w in stopset:
                        continue
                    if w not in dic:
                        dic[w] = 0
                    dic[w] += 1

            except:
                continue
    sort_dic = sorted(dic.items(),key=operator.itemgetter(1))[::-1]
    len_dic = 0
    with open("dictionary", 'w') as f:
        for w in sort_dic:
            if w[1] <= 1 or w[0] == '' or w[0] == 'rt':
                continue
            len_dic += 1
            f.write(w[0]+' '+str(w[1])+'\n')
    print(len_dic)
