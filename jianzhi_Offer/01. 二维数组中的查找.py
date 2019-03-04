#-*- coding:utf-8 -*-
'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for temparr in array:
            low = 0
            high = len(temparr)-1
            while(low<=high):
                mid = (low+high)//2
                if (temparr[mid]==target):
                    return True
                elif temparr[mid]<target:
                    low = mid+1
                else:
                    high = mid -1
        return False     #218ms

    def Find1(self, target, array):
        row = len(array)
        col = len(array[0])
        i = row-1
        j = 0
        while(i>=0 and j<col):
            if(array[i][j]==target):
                return True
            elif array[i][j]> target:
                i -=1
            else:
                j +=1
        return  False         #419ms



#7,[[1,2,8,9],[4,7,10,13]]
#1,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
#16,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

find = Solution().Find1(16,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
print(find)