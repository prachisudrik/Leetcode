#Create another list ->monotonous stack
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack, res = [], [i for i in prices]
        for idx, val in enumerate(prices):
            while stack and prices[stack[-1]] >= val:
                res[stack.pop()] -= val
            stack.append(idx)
        return res

#Second soultion using monotonous increasing stac using same list
def finalPrices(self, A):
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] >= a:
                A[stack.pop()] -= a
            stack.append(i)
        return A
