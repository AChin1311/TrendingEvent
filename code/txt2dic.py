from nltk.corpus import stopwords
import re
import operator
from stoplist import stop_ls 
from nltk.stem import PorterStemmer

if __name__ == '__main__':

    ps = PorterStemmer()

    tweets_data_paths = ["sport","holiday","entertainment","disaster"] 

    stopset = set(stop_ls)
    stopWords = set(stopwords.words('english'))
    dic = {}
    for path in tweets_data_paths:
        tweets_file = open('data/'+path+'.txt', 'r',encoding='utf-8', errors='ignore')
        total_msg = 0
        for line in tweets_file:
            try:
                line_list = line.split(',')       
                text_data = []
                for w in line_list[3].split():
                    if w in stopWords:
                        continue
                    if w in stopset:
                        continue
                    if len(w) == 1:
                        continue
                    if w not in dic:
                        dic[w] = 0
                    dic[w] += 1
            except:
                continue
            
            
        sort_dic = sorted(dic.items(),key=operator.itemgetter(1))[::-1]
        len_dic = 0
        with open("data/"+path+"_dictionary", 'w') as f:
            count = 0
            for w in sort_dic:
                if w[1] <= 100 or w[0] == '' or w[0] == 'rt':
                    continue
                len_dic += 1
                f.write(w[0]+' '+str(w[1])+'\n')
                count += 1
                if count >= 500:
                    break
        print(len_dic)