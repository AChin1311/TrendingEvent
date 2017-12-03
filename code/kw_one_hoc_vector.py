import gensim
from sklearn.cluster import KMeans
import json
from kw import features as kw_features
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import accuracy_score
import operator
from nltk.stem import PorterStemmer

tweets_data_paths = ["holiday.txt"] 

data = []
X = []
label = []
data_dict = {}
ps = PorterStemmer()
holiday_dict = {}

for i in range(len(kw_features['holiday'])):
  holiday_dict[kw_features['holiday'][i]] = i
m = 0
for path in tweets_data_paths:
  print("processing ", path)
  tweets_file = open('data/'+path, 'r',encoding='utf-8', errors='ignore')
  for line in tweets_file:
    try:
      line_list = line.split(',')    
      one_hoc_vec = [0] * len(kw_features['holiday'])
      data.append(line_list[3])
      for w in line_list[3]:
        w = ps.stem(w)
        if w in kw_features['holiday']:
          one_hoc_vec[holiday_dict[w]] += 1
      X.append(one_hoc_vec)
      m+=1
    except:
      continue    

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

my_dict = {}
n = 0
for i,y in enumerate(y_kmeans):
  n += 1
  print(data[i],y)
print(n)

# sort_dic = sorted(my_dict.items(),key=operator.itemgetter(1))
# n = 0
# for w in sort_dic:
#   n+=1
#   print(str(w[1])+' '+w[0])