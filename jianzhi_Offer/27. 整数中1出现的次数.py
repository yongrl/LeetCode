'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # while n>0:
        #     numbers.append(n%10)
        #     n=n//10
        # return numbers
        n_str = str(n)
        num_size = len(n_str)
        count = 0
        for i in range(0,num_size):
            cur_n = int(n_str[i])
            before = n_str[:i]

            if len(before)==0:
                before=0
            else:
                before = int(before)

            after = n_str[i+1:]
            # after主要用来通过字符串长度判断位数，长度的重要性大于数值，如果事先转换为数字，可能会遇见将'000'
            # 转换为0的情况

            if cur_n == 0:
                count += before * pow(10,len(str(after)))
            elif cur_n == 1:
                count += before * pow(10,len(str(after))) + ((0 if after=='' else int(after))+1)
            else:
                count += (before+1) * pow(10,len(str(after)))
        return count

print(Solution().NumberOf1Between1AndN_Solution(10000))

# def search_2(n):
#     res = []
#     for i in range(1,n+1):
#         if (i//10)%10==1:
#             res.append(i)
#
#     #print(res)
#     #print(len(res))
#     return len(res)
#
# def search_1(n):
#     res = []
#     for i in range(1,n+1):
#         if i%10==1:
#             res.append(i)
#
#     #print(res)
#     #print(len(res))
#     return len(res)
#
# def search_3(n):
#     res = []
#     for i in range(1,n+1):
#         if (i//100)%10==1:
#             res.append(i)
#
#     #print(res)
#     #print(len(res))
#     return len(res)
#
# print(search_2(231)+search_1(231)+search_3(231))
