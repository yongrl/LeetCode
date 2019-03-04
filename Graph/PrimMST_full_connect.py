import sys
from collections import defaultdict

from dtw import dtw
from sklearn.metrics import euclidean_distances

from Graph.Heap import Heap
from Graph.Point import Point

class Graph():

    def __init__(self,data):
        self.V=0
        self.edges={}
        self.leftData = data

    # 主函数用来构造最小生死树（MST）
    def PrimMST(self):
        # 存每个节点的key值
        data = self.leftData
        self.V = len(data)

        key = []

        # 记录构造的MST
        parent = []

        # 建立最小堆
        minHeap = Heap()

        # 初始化以上三个数据结构
        for v in range(self.V):
            parent.append(-1)#初始时，每个节点的父节点是-1
            key.append(float('inf'))#初始时，每个节点的key值都是无穷大
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) )
            #newMinHeapNode方法返回一个list，包括节点id、节点key值
            #minHeap.array成员存储每个list，所以是二维list
            #所以初始时堆里的每个节点的key值都是无穷大
            minHeap.pos.append(v)

        minHeap.pos[0] = 0#不懂这句，本来pos的0索引元素就是0啊
        key[0] = 0#让0节点作为第一个被挑选的节点
        minHeap.decreaseKey(0, key[0])
        #把堆中0位置的key值变成key[0]，函数内部重构堆

        # 初始化堆的大小为V即节点个数
        minHeap.size = self.V
        print('初始时array为',minHeap.array)
        print('初始时pos为',minHeap.pos)
        print('初始时size为',minHeap.size)

        while minHeap.isEmpty() == False:

            # 抽取最小堆中key值最小的节点
            newHeapNode = minHeap.extractMin()
            print('抽取了最小元素为',newHeapNode)
            u = newHeapNode[0]

            for i in range(minHeap.size):
                id= minHeap.array[i][0]
                dist = max(0.001,data[u].dtw_dist(data[id]))

                if dist < key[id]:
                    key[id] = dist
                    parent[id] = u

                    # 也更新最小堆中节点的key值，重构
                    minHeap.decreaseKey(id, key[id])
                    self.edges[(u,id)]=dist
                    self.edges[(id,u)]=dist

        print(self.edges)
        edges=[]
        for i in range(1, self.V):
            edges.append((data[parent[i]].getId(),data[i].getId(),self.edges[(parent[i],i)]))

        print(edges)


data =[Point(0,[0,0,1]),Point(1,[0,0,2]),Point(2,[1,0,0]),Point(3,[2,0,2]),Point(4,[1,0,2]),Point(5,[2,2,2]),Point(6,[1,0,2])]
graph = Graph(data=data)
graph.PrimMST()


