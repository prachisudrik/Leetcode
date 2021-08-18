from math import sqrt
import math

ans = 0
def check_if_perfect_square(n):
    if ( sqrt(n) - math.floor(sqrt(n)) ) == 0:
        square_num = n
        return 1
    return 0

def total_count(self,n):
    while(n):
        if (check_if_perfect_square(n)) == 1:
            ans = ans + 1
        else:
            n = n-1
            check_if_perfect_square(n)

n = int(input())
ans = total_count(n)
print(ans)
