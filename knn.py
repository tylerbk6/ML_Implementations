from collections import Counter 
import math 

def knn(data, query, k, distance_fn, choice_fn):
    """ 
    @param data := pairs (X_1,Y_1), ... (X_n,Y_n) in a list
                   (the X_i are features, Y_i are labels)
    @param query := point which distances are calculated from
    @param k := number of neighbours considered in algorithm
    @param distance_fn := metric to use on points
    @param choice_fn := function which gives us value for new datapoint. 
            (mean for regression mode for classification)
    """
    neighbor_distances_and_indices= []
    
    for index, example in enumerate(data):
        # example has the form (feature, label). We want d(feature, query)
        distance = distance_fn(example[:-1], query)

        # add distance and index to list of distances
        neighbor_distances_and_indices.append((distance, index))

    neighbor_distances_and_indices.sort()

    # choose k nearest neighbours
    k_nearest_neighbours = neighbor_distances_and_indices[:k]

    k_nearest_labels = [data[i][1] for distance,i in k_nearest_neighbours]

    return k_nearest_neighbours, choice_fn(k_nearest_labels)

def mean(labels):
    return sum(labels)/len(labels)

def mode(labels):
    return Counter(labels).most_common(1)[0][0]

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)

def main():
    '''
    # Regression Data
    # 
    # Column 0: height (inches)
    # Column 1: weight (pounds)
    '''
    reg_data = [
       [65.75, 112.99],
       [71.52, 136.49],
       [69.40, 153.03],
       [68.22, 142.34],
       [67.79, 144.30],
       [68.70, 123.30],
       [69.80, 141.49],
       [70.01, 136.46],
       [67.90, 112.37],
       [66.49, 127.45],
    ]
    
    # Question:
    # Given the data we have, what's the best-guess at someone's weight if they are 60 inches tall?
    reg_query = [60]
    reg_k_nearest_neighbors, reg_prediction = knn(
        reg_data, reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean
    )
    print(reg_prediction)    

if __name__ == '__main__':
    main()