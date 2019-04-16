'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

@author: yongrl
@date: 20190416

Solution :
find Kth large value
'''

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k>len(tinput):
            return []
        return self.findmid(tinput,0,len(tinput)-1,k-1)

    def partition(self,arr,low,high):
        i = low+1
        j = high
        pivot = low
        while(i<=j):
            while(i<j): # if replace the < of <= ，i may be overflow in the case like:[5,1,2,3] or design more condition
                if arr[i]<= arr[pivot]:
                    i=i+1
                else:
                    break
            while(j>=i):
                if arr[j]>=arr[pivot]:
                    j=j-1
                else:
                    break
            self.swap(arr,pivot,j)
        return j

    def swap(self,arr,i,j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def findmid(self,arr,low,high,k):
        pivot = self.partition(arr,low,high)
        while pivot!=k:
            if pivot < k:
                return self.findmid(arr,pivot+1,high,k)
            else:
                return self.findmid(arr,low,pivot-1,k)
        return arr[:k+1]


print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],10))