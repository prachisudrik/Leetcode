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
                
