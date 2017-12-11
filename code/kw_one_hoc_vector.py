import gensim
from sklearn.cluster import KMeans
import json
from kw import features as kw_features
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import accuracy_score
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
  dictionary_file = open('../data/'+path+'_dictionary.txt', 'r',encoding='utf-8', errors='ignore')
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
  tweets_file = open('../data/'+path+'.txt', 'r',encoding='utf-8', errors='ignore')
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

  # n_clus = int(m/200)
  n_clus = 400
  print("clustering ", path," kmeans  with ",n_clus," clusters")
  y_kmeans = kmean_cos.create_cluster(X, nclust = n_clus)

  n = 0
  y_list = [0]*n_clus
  print("writing ", path, " result to file")
  with open("../data/"+path+"_result.txt", 'w') as f:
    for i,y in enumerate(y_kmeans):
      n += 1
      f.write(str(y))
      f.write(", ")
      f.write(tweets_data[i])
      y_list[y] += 1
      # print(X[i])
    f.write("tweets = "+str(n)+'\n')
    f.write("total clusters = "+str(len(y_list))+'\n')
    f.write("clusters = "+str(y_list)+'\n')
    print("tweets =",n)
    print("total clusters =",len(y_list))
    print("clusters =",y_list)

