class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
                continue
            elif stack[-1] == i.swapcase():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)



class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        stack = [s[0]]
        for i in range(1,len(s)):
            if len(stack) and abs(ord(stack[-1])-ord(s[i])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)
