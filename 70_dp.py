class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one 

#Solution 2
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = sqrt(5)
        fibn = pow((1+sqrt5)/2,n+1)-pow((1-sqrt5)/2,n+1)
        return int(fibn/sqrt5)