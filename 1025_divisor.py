class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2 == 0:
            return 1
#N is even initially,
#1. What is Alice's optimal strategy?
#Choose x = 1, N = N - 1, send the odd back to Bob
#2. What is Bob's optimal strategy?
#Choose x as large as possible to make N reduce as fast as possible such that the pain can #end as early as possible, since nothing will change the fact that he will lose. Just don't #suffer.
#Strategy:
#From above, we know that if Alice meets even N, she will win. So we just need to check if N #is divisble by 2.

