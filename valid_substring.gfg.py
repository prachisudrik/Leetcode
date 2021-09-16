#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here
        stack = []
        for i in S:
            if len(stack) == 0:
                stack.append(i)
                continue
            elif stack[-1] != i:
                stack.pop()
            else:
                stack.append(i)
        return stack



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        S=input()

        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends
