import gensim
from sklearn.cluster import KMeans
import json
from kw import features as kw_features
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import accuracy_score

model = gensim.models.doc2vec.Doc2Vec.load('data/doc2vec.model')
#start testing
#printing the vector of document at index 1 in docLabels
tweets_data_paths = ["1105_compress.json","1104_compress.json"] 
# tweets_data_paths = [ "1103_compress.json","1104_compress.json","1105_compress.json",\
# "1106_compress.json","1107_compress.json","1108_compress.json","1109_compress.json",\
# "1110_compress.json","1112_compress.json","1113_compress.json","1114_compress.json",\
# "1115_compress.json","1116_compress.json","1117_compress.json","1118_compress.json",\
# "1119_compress.json","1120_compress.json","1121_compress.json","1127_compress.json",\
# "1128_compress.json"]

data = []
X = []
label = []

for path in tweets_data_paths:
  print("processing ", path)

  tweets_file = open('data/'+path, 'r',encoding='utf-8', errors='ignore')
  for line in tweets_file:
    try:
      tweet = json.loads(line)
      id = tweet['id_str']
      print(id)
      X.append(model.docvecs[id])

      tw = tweet['text'].lower()
      features_type = [0]*4
      li_type = ['disaster','entertainment','holiday','sport']
      for w in tw.split():
        for i in range(len(li_type)):
          if w in kw_features[li_type[i]]:
            features_type[i] += 1
      label.append(features_type)
      data.append(tw)
    except:
      continue

print(len(X))
print(len(label))
print(len(data))
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
_out = []
_in = []
for i,y in enumerate(y_kmeans):
    _in.append(y)
    for j in range(len(label[i])):
        if label[i][j] !=0:
            _out.append(j)
            break
    print(j, y, data[i])

print(accuracy_score(_in,_out))
print(normalized_mutual_info_score(_in, _out))
