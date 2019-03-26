'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
# -*- coding:utf-8 -*-
import math
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None or len(matrix)==0:
            return matrix
        row = len(matrix)
        col = len(matrix[0])
        circle = math.ceil(row/2) if row <= col else math.ceil(col/2)
        res = []
        for c in range(circle):
            # 左上角坐标
            up_x = c
            up_y = c
            # 右下角坐标
            down_x = row-c
            down_y = col-c
            # 从左向右打印
            for j in range(up_y,down_y):
                res.append(matrix[up_x][j])
            # 判断是都需要从上到下打印
            for i in range(up_x,down_x):
                res.append(matrix[i][down_y-1])
            #从右向左打印
            for j in range(down_y-1,up_y-1,-1):
                res.append(matrix[down_x-1][j])
            #从下到上打印
            for i in range(down_x-1,up_x-1,-1):
                res.append(matrix[i][up_y])

        return res



print(Solution().printMatrix([[1]]))