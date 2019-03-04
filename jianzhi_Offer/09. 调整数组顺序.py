'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reOrderArray(self, array):
        length = len(array)-1
        i=0  #总是指向第一个偶数
        j=0
        while(j<length and i<length):
            while(i<length and array[i]%2==1):
                i+=1
            j = i+1
            while(j<length and array[j]%2==0):
                j+=1
            if(j==length and array[j]%2==0):break
            temp=array[j]
            for k in range(j-1,i-1,-1):
                array[k+1]=array[k]
            array[i]=temp
        return array
s = Solution().reOrderArray([1,2,3,4,5,6,7])
print(s)