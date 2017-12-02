import gensim
from sklearn.cluster import KMeans
model = gensim.models.doc2vec.Doc2Vec.load('doc2vec.model')
#start testing
#printing the vector of document at index 1 in docLabels
X = model.docvecs


kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

for y in y_kmeans:
  print(y)

