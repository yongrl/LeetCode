'''
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字
数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5
'''

class Solution:
    def __init__(self):
        self.count=0

    def InversePairs(self, data):
        if data is None or len(data)<=1:
            return 0
        self.mergeSort(data)
        return self.count%1000000007

    def mergeSort(self, data):
        if len(data) == 1:
            return data
        mid = len(data)//2
        left = self.mergeSort(data[:mid])
        right = self.mergeSort(data[mid:])
        return self.merge(left,right)


    def merge(self,left,right):
        res = []
        r_len = len(right)
        l_len = len(left)
        i, j = 0, 0
        while( i < l_len and j < r_len ):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                self.count += l_len - i
                res.append(right[j])
                j += 1

        while i < l_len:
            res.append(left[i])
            i += 1

        while j < r_len:
            res.append(right[j])
            j += 1


        # for i in range(len(left)):
        #     for j in range(len(right)):
        #         if left[i]>right[j]:
        #             self.count+=1

        return res


s = Solution()
s.InversePairs([1,2,3,4,5,6,7,0])
print(s.count)

#print(Solution().InversePairs([5, 7, 4, 6]))







