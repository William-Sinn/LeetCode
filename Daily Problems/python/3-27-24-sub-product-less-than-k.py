class Solution(object):

    valid_subs = 0

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k <= 1:
            return 0
        
        res = 0
        pro = 1
        left = 0
        for a,b in enumerate(nums):
            pro *= b

            while pro >= k:
                pro /= nums[left]
                left += 1

            res += (a-left) + 1

        return res