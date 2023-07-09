class Solution(object):
    def twoSum(self, nums, target):
        for i ,v in enumerate(nums):
            dd = target -v
            if dd in nums[i+1:]:
                return [i , nums.index(dd ,i+1) ]
