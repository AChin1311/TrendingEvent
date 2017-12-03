import gensim
from sklearn.cluster import KMeans
import json
from kw import features as kw_features
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import accuracy_score
import operator
from nltk.stem import PorterStemmer
import kmeanscosine as kmean_cos
tweets_data_paths = ["holiday"] 

data = []
X = []
label = []
data_dict = {}
ps = PorterStemmer()
holiday_dict = {}
holiday_features = []
holiday_freq = []
for path in tweets_data_paths:
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
# print(holiday_features)
# print(holiday_dict)

m = 0
for path in tweets_data_paths:
  print("processing ", path)
  tweets_file = open('data/'+path+'.txt', 'r',encoding='utf-8', errors='ignore')
  for line in tweets_file:
    try:
      line_list = line.split(',')    
      one_hoc_vec = [0] * len(holiday_dict)
      data.append(line_list[3])
      for w in line_list[3].split():
        if w in holiday_features:
          one_hoc_vec[holiday_dict[w]] = (int(holiday_freq[holiday_dict[w]]))
      X.append(one_hoc_vec)
      m+=1
    except:
      continue    

# kmeans = KMeans(n_clusters=2)
# kmeans.fit(X)
# y_kmeans = kmeans.predict(X)
# print(len(X), len(X[0]))
n_clus = 50
y_kmeans = kmean_cos.create_cluster(X, nclust = n_clus)

n = 0
y_list = [0]*n_clus
for i,y in enumerate(y_kmeans):
  n += 1
  print(y, data[i])
  y_list[y] += 1
  # print(X[i])
print(n)
print(y_list)

