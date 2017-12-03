from sklearn.cluster import k_means_
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances
from sklearn.preprocessing import StandardScaler


def create_cluster(sparse_data, nclust = 10):

    # Manually override euclidean
    def euc_dist(X, Y = None, Y_norm_squared = None, squared = False):
        #return pairwise_distances(X, Y, metric = 'cosine', n_jobs = 10)
        return cosine_similarity(X, Y)
    # k_means_.euclidean_distances = euc_dist
    
    kmeans = k_means_.KMeans(n_clusters = nclust)
    kmeans.euclidean_distances = euc_dist
    print("4")
    _ = kmeans.fit(sparse_data)
    print("5")
    return kmeans.labels_