'''
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
'''
def isPalindrome(strlist):
    i=0
    j=len(strlist)-1
    while(i<j):
        if(strlist[i]!=strlist[j]):
            return False
        i+=1
        j-=1
    return True

def validPalindrome(str):
    strlist=list(str)
    i=0
    j = len(strlist) - 1
    while(i<j):
        if(strlist[i]!=strlist[j]):
            return isPalindrome(strlist[i+1:j])| isPalindrome(strlist[i:j-1])
        i+=1
        j-=1
    return True

if __name__=='__main__':
    print(validPalindrome("abedda"))

