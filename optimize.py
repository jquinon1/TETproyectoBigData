 # clustering dataset
# determine k using elbow method

from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

def getK(vectors):
    # x1 = np.array([3, 1, 1, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8])
    # x2 = np.array([5, 4, 5, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3])
    # x3 = np.array([4, 6, 3, 3, 7, 6, 3, 5, 4, 5, 6, 2, 5, 8 ,8 ,2, 2])
    # ar = [x1,x2,x3]

    # plt.plot()
    # plt.xlim([0, 10])
    # plt.ylim([0, 10])
    # plt.title('Dataset')
    # plt.scatter(x1, x2, x3)
    # plt.show()
    #
    # #create new plot and data
    # plt.plot()
    print(len(vectors[0]))
    print(len(vectors))
    X = np.array(list(zip(vectors))).reshape(len(vectors[0]), len(vectors))


    # k means determine k
    distortions = 1000000
    k = 2
    temp = 0
    while True:
        kmeanModel = KMeans(n_clusters=k).fit(X)
        kmeanModel.fit(X)
        temp = distortions
        distortions = sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0]
        if temp - distortions < temp * 0.2:
            # print("optimo {}".format(k-1))
            return temp
        k = k +1
