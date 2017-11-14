import numpy as np
from tqdm import tqdm
from collections import Counter

class KNearestNeighbor(object):
    """ a kNN classifier with Euclidean distance """

    def __init__(self):
        pass

    def train(self, X, y):
        """
        Train the classifier. For k-nearest neighbors this is just
        memorizing the training data.

        Inputs:
        - X: A numpy array of shape (num_train, D) containing the training data
          consisting of num_train samples each of dimension D.
        - y: A numpy array of shape (N,) containing the training labels, where
             y[i] is the label for X[i].
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X, k=1, num_loops=0):
        """
        Predict labels for test data using this classifier.

        Inputs:
        - X: A numpy array of shape (num_test, D) containing test data consisting
             of num_test samples each of dimension D.
        - k: The number of nearest neighbors that vote for the predicted labels.
        - num_loops: Determines which implementation to use to compute distances
          between training points and testing points.

        Returns:
        - y: A numpy array of shape (num_test,) containing predicted labels for the
          test data, where y[i] is the predicted label for the test point X[i].
        """
        if num_loops == 0:
            dists = self.compute_distances_vectorized(X)
        elif num_loops == 1:
            dists = self.compute_distances_with_loops(X)
        else:
            raise ValueError('Invalid value %d for num_loops' % num_loops)

        return self.predict_labels(dists, k=k)

    def compute_distances_with_loops(self, X):
        """
        Compute the distance between each test point in X and each training point
        in self.X_train using a nested loop over both the training data and the
        test data.

        Inputs:
        - X: A numpy array of shape (num_test, D) containing test data.

        Returns:
        - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
          is the Euclidean distance between the ith test point and the jth training
          point.
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        #####################################################################
        # TODO (5):                                                        #
        # Loop over num_test (outer loop) and num_train (inner loop) and    #
        # compute the Euclidean distance between the ith test point and the #
        # jth training point, and store the result in dists[i, j]. You      #
        # should not use a loop over dimension.                             #
        #####################################################################
        for i in tqdm(range(num_test), ascii=False, desc="euclidean distance calculation"):
            for j in range(num_train):
                diff = self.X_train[j] - X[i]
                dists[i][j] = np.sqrt(np.dot(diff.T, diff))
        #####################################################################
        #                       END OF YOUR CODE                            #
        #####################################################################
        return dists

    def compute_distances_vectorized(self, X):
        """
        Compute the distance between each test point in X and each training point
        in self.X_train using no explicit loops.

        Inputs:
        - X: A numpy array of shape (num_test, D) containing test data.

        Returns:
        - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
          is the Euclidean distance between the ith test point and the jth training
          point.
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        #########################################################################
        # TODO (10):                                                            #
        # Compute the Euclidean distance between all test points and all        #
        # training points without using any explicit loops, and store the       #
        # result in dists.                                                      #
        #                                                                       #
        # You should implement this function using only basic array operations; #
        # in particular you should not use functions from scipy.                #
        #                                                                       #
        # Hint: Try to formulate the Euclidean distance using matrix            #
        #       multiplication and two broadcast sums.                          #
        #########################################################################
        X_train_2 = self.X_train*self.X_train
        X_train_2 = np.sum(X_train_2, axis = 1)

        X_train_2_repeat = np.array([X_train_2]*X.shape[0])

        X_2 = X*X
        X_2 = np.sum(X_2, axis = 1)
        X_2_repeat = np.array( [X_2]*self.X_train.shape[0]).transpose()

        X_dot_X_train = X.dot(self.X_train.T)

        dists = X_train_2_repeat + X_2_repeat - 2*X_dot_X_train
        dists = np.sqrt(dists)
        
        
        return dists
        #########################################################################
        #                         END OF YOUR CODE                              #
        #########################################################################
        return dists

    def most_common(self, arr):
        results = Counter(arr).most_common(1)[0] # return all most common elements - draws (element, amount of occurrence)
        if (type(results) is np.ndarray):
            result = min(results)
            #example result = [(2, 2), (5, 2)]
            #occurence (second element) is always the same, therefore only the label differs
        else:
            result = results
            
        return result[0]
        #return only the label
    
    def predict_labels(self, dists, k=1):
        """
        Given a matrix of distances between test points and training points,
        predict a label for each test point.

        Inputs:
        - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
          gives the distance betwen the ith test point and the jth training point.

        Returns:
        - y: A numpy array of shape (num_test,) containing predicted labels for the
          test data, where y[i] is the predicted label for the test point X[i].
        """
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)
        for i in range(num_test):
            # A list of length k storing the labels of the k nearest neighbors to the ith test point.
            closest_y = []
            #########################################################################
            # TODO (2):                                                             #
            # Use the distance matrix to find the k nearest neighbors of the ith    #
            # testing point, and use self.y_train to find the labels of these       #
            # neighbors. Store these labels in closest_y.                           #
            # Hint: Look up the function numpy.argsort.                             #
            #########################################################################                
            nearest_index = np.argsort(dists[i])[:k] #0 to k-1
            closest_y = self.y_train[nearest_index]
            #########################################################################
            # TODO (2):                                                             #
            # Now that you have found the labels of the k nearest neighbors, you    #
            # need to find the most common label in the list closest_y of labels.   #
            # Store this label in y_pred[i]. Break ties by choosing the smaller     #
            # label.                                                                #
            #########################################################################
            y_pred[i] = self.most_common(closest_y)
            #########################################################################
            #                           END OF YOUR CODE                            #
            #########################################################################
        return y_pred