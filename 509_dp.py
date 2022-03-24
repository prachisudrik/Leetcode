class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        arr1 = [0] * (n+1)
        arr1[1] = 1
        for i in range(2,n+1):
            arr1[i] = arr1[i-1] + arr1[i-2]
        return arr1[-1]