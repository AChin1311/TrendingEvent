import gensim
from sklearn.cluster import KMeans
import json
from kw import features as kw_features
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import accuracy_score
import operator

model = gensim.models.doc2vec.Doc2Vec.load('data/doc2vec_txt.model')

tweets_data_paths = ["holiday.txt"] 

data = []
X = []
label = []
data_dict = {}

for path in tweets_data_paths:
  print("processing ", path)
  tweets_file = open('data/'+path, 'r',encoding='utf-8', errors='ignore')
  for line in tweets_file:
    try:
      line_list = line.split(',')       
      id = line_list[0]
      X.append(model.docvecs[id])
      data.append(line_list[3])
      data_dict[line_list[3]] = line_list[2]
    except:
      continue

kmeans = KMeans(n_clusters=10)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

my_dict = {}
for i,y in enumerate(y_kmeans):
  my_dict[data[i]] = y
sort_dic = sorted(my_dict.items(),key=operator.itemgetter(1))
for w in sort_dic:
  print(str(w[1])+' '+w[0]+str(data_dict[w[0]]))
