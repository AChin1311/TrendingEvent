from sklearn.cluster import k_means_
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances
from sklearn.preprocessing import StandardScaler


def create_cluster(sparse_data, nclust = 10):

    # Manually override euclidean
    def euc_dist(X, Y = None, Y_norm_squared = None, squared = False):
        #return pairwise_distances(X, Y, metric = 'cosine', n_jobs = 10)
        return cosine_similarity(X, Y)
    k_means_.euclidean_distances = euc_dist
    
    scaler = StandardScaler(with_mean=False)
    sparse_data = scaler.fit_transform(sparse_data)
    kmeans = k_means_.KMeans(n_clusters = nclust, n_jobs = 20, random_state = 3425)
    _ = kmeans.fit(sparse_data)
    return kmeans.labels_