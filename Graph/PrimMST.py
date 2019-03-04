import sys
import numpy as np

from Graph import Edge


class PrimMST(object):

    def __init__(self,vertexs,edges):
        self.verts = vertexs
        self.edges = edges
        self.T = np.zeros((self.verts,self.verts))
        for edge in edges:
            i = edge.getU()
            j = edge.getV()
            self.T[i,j] = edge.getWeight()
            self.T[j,i] = edge.getWeight()

        # 使用parent[]来打印MST
    def printMST(self, parent):
        print("Edge \tWeight")
        # 打印每个点与父节点的边就可以了，注意根节点不用打印
        for i in range(1, self.verts):
            print(parent[i], "-", i, "\t", self.T[i][parent[i]])

    def getMinKey(self,key,mstSet):
        min = sys.float_info.max

        for v in range(self.verts):
            if key[v] < min and mstSet[v] == False:
                # False代表是非MST集合中的节点，然后就是普通的寻找最小的操作
                min = key[v]
                min_index = v

        return min_index


    def MST(self):
        key = [sys.float_info.max]*self.verts
        parent = [None]*self.verts
        key[0] = 0
        mstSet = [False]*self.verts
        parent[0] = -1

        for cout in range(self.verts):


            # 从非MST集合中挑选最小距离的节点
            u = self.getMinKey(key,mstSet)

            # 把挑选到的节点放到MST集合中去
            mstSet[u] = True

            #更新
            for v in range(self.verts):
                # self.graph[u][v] > 0代表v是u的邻接点
                # mstSet[v] == False代表当前节点还没有加入到MST中
                # key[v] > self.graph[u][v]只有新距离比当前记录距离要小时更新
                # 两种情况，一是key[v]为无穷，肯定更新；二是key[v]为常数，但新距离更小
                if (self.T[u][v] > 0) and (mstSet[v] == False) and (key[v] > self.T[u][v]):
                    key[v] = self.T[u][v]  # 更新距离
                    parent[v] = u  # 更新父节点

        self.printMST(parent)


if __name__=='__main__':
    edges=[Edge(0,1,2),Edge(0,3,6),Edge(1,2,3),Edge(1,3,8),Edge(1,4,5),Edge(2,4,7),Edge(3,4,9)]
    print(PrimMST(5, edges).MST())








