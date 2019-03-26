import sys
#sys.setrecursionlimit(2140000000)
import time


class N_Queue():
    def __init__(self,N):
        self.N = N
        self.board = []
        self.sol=0

    # 愚蠢的递归形式
    def putQueue(self,col):
        if len(self.board)==self.N:
            self.sol+=1
            print("solution %d"%self.sol)
            print(self.board)
            col = self.board.pop(-1)
            self.putQueue(col+1)
            return

        if col==self.N:
            if len(self.board)==0:
                return
            else:
                col = self.board.pop(-1)
                self.putQueue(col+1)
                return
        if self.isSafe(col):
            self.board.append(col)
            self.putQueue(0)
            return
        else:
            self.putQueue(col+1)
            return

    # 改进的递归形式
    def putQueue_update(self,row):
        if row==self.N:
            self.sol+=1
            print("solution %d"%self.sol)
            print(self.board)
        else:
            for i in range(self.N):
                if self.isSafe(i):
                    self.board.append(i)
                    self.putQueue_update(row+1)
                    self.board.pop(-1)

    # 非递归形式
    def putQueue_nonRecursive(self):
        stack = []           # stack用来存储下一次遍历的节点
        stack.append((0,0))  # 初始为(0,0)
        while len(stack)>0:
            row,col = stack.pop(-1)

            if col==self.N and len(stack)==0:     #遍历为所有节点
                break
            if col==self.N:          #列遍历完，返回上一行，此时需要将board中的上一行的皇后位置抹掉
                self.board.pop(-1)
                continue

            if self.isSafe(col):     # 如果该节点是安全的
                self.board.append(col)    # 将位置记录到board中
                if len(self.board) == self.N:   #如果board的所有行都记录了，输入该种皇后摆法
                    self.sol+=1
                    print("solution %d"%self.sol)
                    print(self.board)
                stack.append((row,col+1))   # stack记录下次遍历的节点，列优先
                stack.append((row+1,0))     # 行
            else:
                stack.append((row,col+1))   # 位置不安全，继续列搜索

    def isSafe(self,col):
        row,col = len(self.board),col
        #判断列
        if col in self.board:
            return False
        #判断对角线
        for i in range(len(self.board)):
            j = self.board[i]
            if abs(i-row)==abs(j-col):
                return False
        return True

    def printBoard(self):
            print(self.board)

start_time = time.time()
N_Queue(10).putQueue_nonRecursive()
end_time = time.time()
print("time: %s"%str(end_time-start_time))



