'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.

思路：

1. python 自带函数s.count(i)
2. list(tuple(value,count)) 遍历一遍数组基数,还是用hash吧，这个用字典，不能保证顺序，用list+tuple不好访问内部值
3. hash
有两种hash方式,一种直接hash为256个assic码,
另一种hash为58个桶，因为A-Z为65-90,a-z为97-122，每个字符对应的hash值为ord(s)-65
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        if s is None or len(s)==0:
            return -1
        for i in s:
            if s.count(i)==1:
                break
        return s.index(i)

    def FirstNotRepeatingChar_hash(self, s):
        if s is None or len(s)==0:
            return -1
        counts = [0]*58
        for i in s:
            counts[ord(i)-65]+=1

        for j in s:
            if counts[ord(j)-65]==1:
                break
        return s.index(j)




print(Solution().FirstNotRepeatingChar_hash('google'))