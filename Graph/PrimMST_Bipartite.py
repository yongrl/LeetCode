import sys
from collections import defaultdict

from dtw import dtw
from sklearn.metrics import euclidean_distances

from Graph.Heap import Heap
from Graph.Point import Point

class Graph():

    def __init__(self,left_data,right_data):
        self.V=0
        self.edges={}
        self.leftData = left_data
        self.rightData = right_data

    def side_label(self,index,num_left,num_right):
        if index in range(0,num_left):
            return 'left'
        if index in range(num_left,num_left+num_right):
            return 'right'

    # 主函数用来构造最小生死树（MST）
    def BipartiteMST(self):
        # 存每个节点的key值
        left_data = self.leftData
        right_data = self.rightData


        num_left = len(left_data)
        num_right = len(right_data)


        key_left = []
        key_right = []

        # 记录构造的MST
        parent_left = []
        parent_right =[]

        # 建立最小堆
        minHeap_left = Heap()
        minHeap_right =Heap()


        # 初始化左节点三个数据结构
        for v in range(num_left):
            parent_left.append(-1)#初始时，每个节点的父节点是-1
            key_left.append(float('inf'))#初始时，每个节点的key值都是无穷大
            minHeap_left.array.append( minHeap_left.newMinHeapNode(v, key_left[v]))
            #newMinHeapNode方法返回一个list，包括节点id、节点key值
            #minHeap.array成员存储每个list，所以是二维list
            #所以初始时堆里的每个节点的key值都是无穷大
            minHeap_left.pos.append(v)

        # 初始化右节点三个数据结构
        for v in range(num_right):
            parent_right.append(-1)#初始时，每个节点的父节点是-1
            key_right.append(float('inf'))#初始时，每个节点的key值都是无穷大
            minHeap_right.array.append( minHeap_right.newMinHeapNode(v, key_right[v]))
            minHeap_right.pos.append(v)



        minHeap_left.pos[0] = 0#不懂这句，本来pos的0索引元素就是0啊
        key_left[0] = 0#让0节点作为第一个被挑选的节点
        minHeap_left.decreaseKey(0, key_left[0])
        #把堆中0位置的key值变成key[0]，函数内部重构堆

        minHeap_right.pos[0] = 0
        #key_right[0] = 0
        minHeap_right.decreaseKey(0, key_right[0])



        # 初始化堆的大小为V即节点个数
        minHeap_left.size = num_left
        minHeap_right.size = num_right
        print('初始时array为',minHeap_left.array)
        print('初始时pos为',minHeap_left.pos)
        print('初始时size为',minHeap_left.size)

        label ='left'
        while minHeap_left.isEmpty() == False | minHeap_right.isEmpty() == False:
            # 抽取最小堆中key值最小的节点
            if label=='left':
                newHeapNode = minHeap_left.extractMin()
                print('left抽取了最小元素为',newHeapNode)
                u = newHeapNode[0]

                for i in range(minHeap_right.size):
                    id= minHeap_right.array[i][0]
                    dist = max(0.001,left_data[u].dtw_dist(right_data[id]))
                    if dist < key_right[id]:
                        key_right[id] = dist
                        parent_right[id] = u

                        # 也更新最小堆中节点的key值，重构
                        minHeap_right.decreaseKey(id, key_right[id])


                        self.edges[(u,id)]=dist

                label='right'
            else:
                newHeapNode = minHeap_right.extractMin()
                print('right抽取了最小元素为',newHeapNode)
                v = newHeapNode[0]

                for i in range(minHeap_left.size):
                    id= minHeap_left.array[i][0]
                    dist = max(0.001,right_data[v].dtw_dist(left_data[id]))
                    if dist < key_left[id]:
                        key_left[id] = dist
                        parent_left[id] = v

                        # 也更新最小堆中节点的key值，重构
                        minHeap_left.decreaseKey(id, key_left[id])

                        self.edges[(id,v)]=dist
                label='left'


        print(self.edges)
        edges=[]
        print("parent_left:",parent_left)
        print("parent_right:",parent_right)
        for i in range(1, num_left):
            edges.append((right_data[parent_left[i]].getId(),left_data[i].getId(),self.edges[(i,parent_left[i])]))

        for j in range(0,num_right):
            edges.append((left_data[parent_right[j]].getId(),right_data[j].getId(),self.edges[(parent_right[j],j)]))


        print(edges)


leftdata =[Point(0,[0,0,1]),Point(1,[0,0,2]),Point(2,[1,0,0]),Point(3,[2,0,2]),Point(4,[1,0,2])]
rightdata=[Point(5,[2,2,2]),Point(6,[1,0,2]),Point(7,[8,9,10])]
graph = Graph(leftdata,rightdata)
graph.BipartiteMST()


