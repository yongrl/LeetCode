# -*- coding:utf-8 -*-
'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

# 先列出所有可能，然后在排序
class Solution:
    def Permutation(self, ss):
        #self.ss = sorted(ss)
        res = self.helper(ss)
        res = sorted(res)
        print(res)
        return res

    def helper(self,str):
        res=[]
        if len(str)==1:
            res.append(str)
        else:
            for i in range(len(str)):
                cur_str = str[0]
                pre_res = self.helper(str[1:])
                for str in pre_res:
                    for i in range(len(str)):
                        temp = str[:i]+cur_str+str[i:]
                        if temp not in res:
                            res.append(str[:i]+cur_str+str[i:])
                    temp = str+cur_str
                    if temp not in res:
                        res.append(str+cur_str)
                break
        return res

# 试图按顺序排列
class Solution_1:
    def Permutation(self, ss):
        if ss is None or len(ss)==0:
            return []
        ss = sorted(ss)
        ss = ''.join(ss)
        res = self.helper([('',ss)])
        res = [tup[0]+tup[1] for tup in res]
        print(res)
        return res

    def helper(self,str_list):
        res=[]
        for tup in str_list:
            pre,next = tup[0],tup[1]
            if next=='':
                return str_list
            for c in next:
                tup = (pre+c,next.replace(c,'',1))
                if tup not in res:
                    res.append(tup)
        return self.helper(res)




Solution_1().Permutation(ss ='abbc')