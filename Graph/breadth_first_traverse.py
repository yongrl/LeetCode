'''
广度优先遍历是连通图的一种遍历策略，其基本思想：

1、从图中某个顶点V0出发，并访问此顶点；

2、从V0出发，访问V0的各个未曾访问的邻接点W1，W2，…,Wk;然后,依次从W1,W2,…,Wk出发访问各自未被访问的邻接点；

3、重复步骤2，直到全部顶点都被访问为止

实现技术点：
1.使用一个临时栈保存每层访问点
'''
import numpy as np


'''方式一:只保存边对'''


'''方式二:以二维数组保存边'''
class Graph(object):

    def __init__(self,V):
        '''
        初始化图
        :param V: 节点个数
        '''
        self.V=V
        self.graph = np.zeros((V,V))
        self.node = []

    def addEgde(self,u,v,w=1):
        '''
        为图添加边
        :param u: 边的起始点
        :param v: 边的结束点
        :param w: 默认值为1，表示u,v之间有连接，赋值则便是边的权重
        :return:
        '''
        if u not in self.node:
            self.node.append(u)

        if v not in self.node:
            self.node.append(v)

        #将节点名u转换为index
        u = self.node.index(u)
        v = self.node.index(v)
        self.graph[u][v]=w

    def BFT(self):
        '''
        广度遍历
        :return: nodes,list
        '''
        V=len(self.node)
        #选择起始点

        #存储已经访问过的点
        visited=[0]
        #临时栈 保存层节点

        temp=[0]

        while True:
            temp_1=[]
            while len(temp)!=0:
                node = temp.pop(0)
                for j in range(self.V):
                    if self.graph[node][j]!=0:
                        if j not in visited:
                            visited.append(j)
                            temp_1.append(j)
            if(len(visited)==self.V):
                break
            temp=temp_1

        print(visited)


#测试案例
graph=Graph(5)
graph.addEgde(3,9)
graph.addEgde(3,20)
graph.addEgde(20,15)
graph.addEgde(20,7)
print("graph:",graph.graph)
graph.BFT()

'''方式三:非连通图，即存在多棵树'''




