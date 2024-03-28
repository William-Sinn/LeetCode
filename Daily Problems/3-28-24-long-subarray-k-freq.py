class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        key_dict = {}
        i = 0

        for num in nums:
            if num not in key_dict:
                key_dict[num] = 1
            else:
                key_dict[num] += 1

            freq = key_dict[num]

            if freq > k:
                return(i)
            else:
                i += 1

        return i
