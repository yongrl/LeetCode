from collections import defaultdict

from Graph.Heap import Heap


def printArr(parent, n):
    for i in range(1, n):
        print ("% d - % d" % (parent[i], i))


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # 添加无向图的每条边
    def addEdge(self, src, dest, weight):

        # 当前边从src到dest，权值为weight
        # 添加到src的邻接表中，添加元素为[dest, weight]
        # 注意都是添加到0索引位置
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # 因为是无向图，所以反向边也得添加
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    # 主函数用来构造最小生死树（MST）
    def PrimMST(self):
        # V是节点的个数
        V = self.V

        # 存每个节点的key值
        key = []

        # 记录构造的MST
        parent = []

        # 建立最小堆
        minHeap = Heap()

        # 初始化以上三个数据结构
        for v in range(V):
            parent.append(-1)#初始时，每个节点的父节点是-1
            key.append(float('inf'))#初始时，每个节点的key值都是无穷大
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) )
            #newMinHeapNode方法返回一个list，包括节点id、节点key值
            #minHeap.array成员存储每个list，所以是二维list
            #所以初始时堆里的每个节点的key值都是无穷大
            minHeap.pos.append(v)
            #pos成员添加每个节点id
        #minHeap.pos初始时是0-8，都小于9即节点数

        minHeap.pos[0] = 0#不懂这句，本来pos的0索引元素就是0啊
        key[0] = 0#让0节点作为第一个被挑选的节点
        minHeap.decreaseKey(0, key[0])
        #把堆中0位置的key值变成key[0]，函数内部重构堆

        # 初始化堆的大小为V即节点个数
        minHeap.size = V
        print('初始时array为',minHeap.array)
        print('初始时pos为',minHeap.pos)
        print('初始时size为',minHeap.size)

        # 最小堆包含所有非MST集合中的节点
        # 所以当最小堆为空，循环终止
        while minHeap.isEmpty() == False:

            # 抽取最小堆中key值最小的节点
            newHeapNode = minHeap.extractMin()
            print('抽取了最小元素为',newHeapNode)
            u = newHeapNode[0]

            # 遍历所有的邻接点然后更新它们的key值
            for pCrawl in self.graph[u]:

                v = pCrawl[0]

                # 如果v在当前最小堆中，且新的key值比当前key值更小，就更新
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u

                    # 也更新最小堆中节点的key值，重构
                    minHeap.decreaseKey(v, key[v])

        printArr(parent, V)

graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.PrimMST()
