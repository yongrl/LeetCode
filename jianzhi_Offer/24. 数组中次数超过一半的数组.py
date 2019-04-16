'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

@Author: yongrl

Solution:
1. loop the number list and construct a map to store (value，count) map and then check　the number,
    and the time complex is O(n)

2. use Partition function which is the core idea in quick sort to find the (length//2) value and
    then chen check the number of the this value.
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        return self.findmid(numbers,0,len(numbers)-1,len(numbers))


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

    def findmid(self,arr,low,high,length):
        pivot = self.partition(arr,low,high)
        while pivot!=length//2:
            if pivot < length//2:
                return self.findmid(arr,pivot+1,high,length)
            else:
                return self.findmid(arr,low,pivot-1,length)
        if self.check(arr,pivot):
            return arr[pivot]
        else:
            return 0

    def check(self,arr,pivot):
        length = len(arr)
        count=0
        for i in arr:
            if i==arr[pivot]:
                count+=1
        if count>length//2:
            return True
        else:
            return False

print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))