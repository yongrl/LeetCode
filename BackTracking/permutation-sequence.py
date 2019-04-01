class Solution(object):
    def __init__(self):
        self.permu = []
        self.s=''

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """


    def Permutation(self,i):
        if len(self.s)==self.N:
            self.permu.append(self.s)
        for i in range(1,self.N+1):
            if str(i) not in self.s:
                self.s=self.s+str(i)
                self.Permutation(i+1)
                self.s=self.s[:-1]

    def Permutation_noRecursive(self):
        stack = [('',1)]
        while len(stack)>0:
            s, d = stack.pop(-1)

            if d>self.N and len(stack)==0:
                break

            if d>self.N:   #
                #stack.pop(-1)
                continue

            if str(d) in s:
                stack.append((s,d+1))
            else:
                temp_s = s+str(d)
                if len(temp_s)==self.N:
                    self.permu.append(temp_s)
                else:
                    stack.append((s,d+1))
                    stack.append((temp_s,1))



print(Solution().getPermutation(9, 24))




