import numpy as np
from sklearn.cluster import KMeans
import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
dim = 0

def getCentroid(cluster):
  total = [0]*dim
  for p in cluster:
    for i in range(len(p)):
      total[i] += p[i]
  for i in range(len(total)):
    total[i] /= len(cluster)
  return total

def distance(x, y):
  return np.dot(np.array(x),np.array(y))

def reassignClusters(dataSet, centroids, clusters):
  for cl in clusters:
    cl = []
  for p in dataSet:  
    dists = [0]*len(centroids)
    for c in centroids:
      dists.append(distance(p, c))
    c_indx = dists.index(min(dists))
    clusters[c_indx].append(p)


K = 5
if __name__ == '__main__':
  dataSet = np.load('data/doc_vec.npy').tolist()
  print(len(dataSet))
  print(len(dataSet[0]))
  dim = len(dataSet[0])
  clusters = []
  k = 0
  while k < K:
      cluster = []
      clusters.append(cluster)
      k += 1
  
  # Initially randomly assign points to clusters
  part = len(dataSet)//K
  i = 0
  for c in clusters:
    for index in range(i,min(len(dataSet), i+part)):
      c.append(dataSet[index])
    # c = set(dataSet[i:min(len(dataSet), i+part)])
    i += part 

  # calculate centroid for clusters
  centroids = []
  for j in range(K):
    centroids.append(getCentroid(clusters[j]))

  for j in range(K):
    clusters[j] = []

  reassignClusters(dataSet, centroids, clusters)
  
  # continue till converge
  iteration = 0
  while True:
    iteration += 1
    # calculate centroid for clusters
    centroidsNew = []
    for j in range(K):
      centroidsNew.append(getCentroid(clusters[j]))

    isConverge = False
    for j in range(K):
      if compare(centroidsNew[j], centroids[j]):
        isConverge = False
      else:
        isConverge = True
    if isConverge:
      break

    for j in range(K):
      clusters[j] = []

    reassignClusters(dataSet, centroidsNew, clusters)
    for j in range(K):
      centroids[j] = centroidsNew[j]

  print("Iteration :" + str(iteration))

  for c in clusters:
    print(len(c))  