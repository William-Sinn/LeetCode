class Solution(object):
    def firstMissingPositive(self, nums):
        nums = set(nums)

        for x in range(1, len(nums) + 2):
            if x not in nums:
                return x