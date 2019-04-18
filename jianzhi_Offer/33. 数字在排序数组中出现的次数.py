'''
很简单的方法可以解决，但是这里想要考二分查找
使用二分查找找出K第一次出现的地方和最后一次出现的地方

@Author: yongrl
@Date : 2019/04/18
'''

class Solution:
    def GetNumberOfK(self, data, k):
        if data is None and len(data)==0:
            return 0
        firstK = self.getFirstK(data,k)
        lastK = self.getLastK(data,0,len(data)-1,k)

        if firstK==-1:
            return 0
        return lastK-firstK+1


    # 循环写法
    def getFirstK(self,data,k):
        low = 0
        high = len(data)-1
        while( low <= high):
            mid = (low + high) >> 1
            if data[mid] == k and mid>0:
                if data[mid-1] == k:
                    high = mid-1
                else:
                    return mid
            if data[mid] == k and mid ==0 :
                return mid
            if data[mid]>k:
                high = mid -1
            if data[mid]<k:
                low = mid + 1
        return -1

    # 递归写法
    def getLastK(self,data,low,high,k):
        if low>high:
            return -1

        mid = (low+high)>>1
        if data[mid] > k:
            return self.getLastK(data,low,mid-1,k)
        if data[mid] < k:
            return self.getLastK(data,mid+1,high,k)
        if data[mid] == k:
            if mid < high and data[mid+1]==k:
                return self.getLastK(data,mid+1,high,k)
            if mid < high and data[mid+1]!=k:
                return mid
            if mid==high:
                return mid



print(Solution().GetNumberOfK([1,2,3,3,3,3,4,5],3))




