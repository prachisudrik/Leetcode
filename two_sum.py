class Solution:
    def twoSum(self,nums, target):
	    for i, num in enumerate(nums):
		    pair = target - num
		    if pair in nums[i + 1:]:
			    return [i, nums.index(pair, i + 1)]

