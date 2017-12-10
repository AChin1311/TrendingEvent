import gensim
from sklearn.cluster import KMeans
import json
from kw import features as kw_features
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import accuracy_score
from sklearn.cluster import DBSCAN
from sklearn import metrics
import operator
from nltk.stem import PorterStemmer
import kmeanscosine as kmean_cos

tweets_data_paths = ["sport"\
#,"holiday","entertainment","disaster"\
] 


for path in tweets_data_paths:
  data = []
  tweets_data = []
  X = []
  label = []
  holiday_dict = {}
  holiday_features = []
  holiday_freq = []
  print("processing ", path," dictionary")
  dictionary_file = open('data/'+path+'_dictionary', 'r',encoding='utf-8', errors='ignore')
  i = 0
  for line in dictionary_file:
    try:
      line_list = line.split()
      holiday_features.append(line_list[0])
      holiday_dict[line_list[0]] = i
      holiday_freq.append(line_list[1])
      i += 1
    except:
      continue

  m = 0
  print("building ", path," vector")
  tweets_file = open('data/'+path+'.txt', 'r',encoding='utf-8', errors='ignore')
  for line in tweets_file:
    try:
      line_list = line.split(',')    
      one_hoc_vec = [0] * len(holiday_dict)
      data.append(line_list[3])
      #print(tweets_data)
      tweets_data.append(line)
      for w in line_list[3].split():
        if w in holiday_features:
          one_hoc_vec[holiday_dict[w]] = (int(holiday_freq[holiday_dict[w]]))
      X.append(one_hoc_vec)
      m+=1
    except:
      continue    

  db = DBSCAN(eps=100, min_samples=10).fit(X)
  labels = db.labels_
  with open("kmeans_result/dbscan_"+path+"_result", 'w') as f:
    for i in range(len(labels)):
      f.write(str(labels[i]) + ", ")
      f.write(tweets_data[i])

  db_data = open("kmeans_result/dbscan_"+path+"_result", 'r',encoding='utf-8', errors='ignore')
  db_dict = {}
  for line in db_data:
    try:
      line_list = line.split(',')    
      if line_list[0] == -1:
        continue
      if line_list[0] not in db_dict:
        db_list = []
        db_list.append(line_list[4])
        db_dict[line_list[0]] = db_list
      else:
        db_dict[line_list[0]].append(line_list[4])
    except: 
      continue

  db_dict_index = sorted(db_dict, key=lambda x: len(db_dict[x]), reverse=True) 

  with open("kmeans_result/dbscan_"+path+"_ranking_result", 'w') as f:
    for i in range(len(db_dict_index)):
      index = db_dict_index[i]
      f.write(str(index) + ", ")
      f.write(str(len(db_dict[index])) + ", ")
      f.write(db_dict[index][0])

  # with open("kmeans_result/"+"ranking_result", 'w') as f:
  #     for i in range(20):
  #         f.write(str(i+1)+ ". "+str(vals[sort_index[len(vals)-i-1]]) + ", ")
  #         text = tweet[str(sort_index[len(vals)-i-1])].split(',')
  #         f.write(tweet[str(sort_index[len(vals)-i-1])])
  #         f.write("\n")