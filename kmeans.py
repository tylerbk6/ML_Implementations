import math
import random 

def kmeans(data, k, distance_fn, max_iterations, tolerance=.0001):
    """
    @param data := unlabelled data (X_1), ... (X_n) in a list
    @param k := the number of clusters to create
    @param distance_fn := metric to use on points
    @param max_iterations := max number of iterations for the algorithm to run for
    @param tolerance := tolerance value we will accept for stopping condition, set
    by default to 0.0001
    """
    initial_centroids=random.sample(data,k)
    clusters={}
    for d in data:
        clusters[d]=argmin([distance_fn(d,c) for c in centroids])
        


def argmin(list):
    min=10000
    for i in list:
        if list[i]<min:
            min=list[i]
    return min
