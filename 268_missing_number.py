class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        original_sum= (n*(n+1))/2
        current_sum=sum(nums)
        missing_num = original_sum - current_sum
        return int(missing_num)