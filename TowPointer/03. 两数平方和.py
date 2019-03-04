'''
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
题目描述：判断一个数是否为两个数的平方和。
'''
from math import floor, sqrt

def judgeSquareSum(target):
    i=1
    j=floor(sqrt(target))
    while(i<j):
        ssum=i*i+j*j
        if ssum==target:
            return True
        if ssum>target:
            j-=1
        if ssum<target:
            i+=1
    return False

if __name__=='__main__':
    print(judgeSquareSum(9))