'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray)==0:
            return 0
        min = rotateArray.pop(0)
        for i in range(len(rotateArray)):
            if rotateArray[i]<min:
                min = rotateArray[i]
        return min                 #671ms

    def minNumberInRotateArray1(self, rotateArray):
        low = 0
        high = len(rotateArray)-1
        while(low<high):
            if high-low==1:
                return rotateArray[high]
            mid = (low+high)//2
            if rotateArray[mid]>=rotateArray[high]:
                low = mid
            else:
                high = mid

        return rotateArray[high]   #1000ms

s=Solution()
print(s.minNumberInRotateArray1([2,3,4,5,1]))

