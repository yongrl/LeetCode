from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

from dtw import dtw

try:
    import cPickle as pickle
except ImportError:
    import pickle

class Point():
    def __init__(self,id=None,coords=None):
        self.id = id
        self.coords = coords

    def getDimension(self):
        return len(self.coords)

    def getId(self):
        return self.id

    def getCoords(self):
        return self.coords

    def write(self,output):
        f = open(output, 'wb')
        pickle.dump(self, f)
        f.close()

    def read(self,input):
        f = open(input, 'rb')
        point = pickle.load(f)
        f.close()
        return point

    def dtw_dist(self,other,dist = euclidean_distances,warp=1):
        x = np.array(self.coords)
        y = np.array(other.coords)
        dist, cost, acc, path = dtw(x, y, dist=lambda a, b: abs(a-b))
        return dist

    def sdtw_dist(self,other,dist = euclidean_distances,warp=1):
        pass