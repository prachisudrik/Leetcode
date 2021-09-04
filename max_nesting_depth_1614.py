class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append(i)
                count += 1
                if max_depth < count:
                    max_depth = count
            elif i == ")":
                stack.pop()
                count -= 1
        return max_depth
