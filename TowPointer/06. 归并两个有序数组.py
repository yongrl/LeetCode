'''
归并两个有序数组

88. Merge Sorted Array (Easy)

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
题目描述：把归并结果存到第一个数组上。

需要从尾开始遍历，否则在 nums1 上归并得到的值会覆盖还未进行归并比较的值。
'''

def merge_sorted_array(nums1,nums2,m,n):
    i=m-1
    j=m-1
    k=len(nums1)-1
    while(i>=0|j>=0):
        if(nums1[i]<nums2[j]):
            nums1[k]=nums2[j]
            j-=1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1
    while i>=0:
        nums1[k]=nums1[i]
        i -= 1
        k -= 1
    while j>=0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1

if __name__=='__main__':
    print(merge_sorted_array([3, 4, 5, 0, 0, 0], [2, 5, 6], 3, 3))

