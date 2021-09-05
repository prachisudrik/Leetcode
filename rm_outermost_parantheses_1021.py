#Solution 1 without using stack
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt, res = 0, ''
        for c in S:
            if c == ')': cnt -= 1
            if cnt != 0: res += c
            if c == '(': cnt+=1
        return res

# Solution with stack
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        len1 = len(s)-1
        index = 0
        stack = []
        res = ""
        while index <= len1:
            if s[index] == '(':
                stack.append(index)
            elif s[index] == ')':
                start = stack.pop()
            if not stack:
                res = res + s[start+1:index]
            index += 1
        return res

#Third Solution
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        count = 0
        first = 0
        for i in range(len(S)):
            if S[i] == "(":
                count +=1
            else:
                count -= 1

            if(count == 0):
                res +=(S[first+1:i])
                first = i+1
        return res
