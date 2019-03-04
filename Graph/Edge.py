class Edge(object):

    def __init__(self,end1=None,end2=None,weight=None):
        self.u = end1
        self.v = end2
        self.weight = weight

    def setWeight(self,weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def getU(self):
        return self.u

    def getV(self):
        return self.v