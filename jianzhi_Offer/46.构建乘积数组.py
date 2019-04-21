'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''
class Solution:
    def multiply(self, A):
        if A is None or len(A)==0:
            return []
        size = len(A)
        B = [1]*size
        C = [1]*size

        for i in range(0,size-1):
            B[i+1] = B[i]*A[i]

        for i in range(size-1,0,-1):
            C[i-1] = C[i]*A[i]

        for i in range(size):
            B[i] = B[i]*C[i]

        return B