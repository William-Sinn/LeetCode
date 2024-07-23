class Solution(object):
    def minOperations(self, nums):
        nums_len = len(nums)
        ops = nums_len
        new_nums = sorted(set(nums))
        right = 0

        for left in range(len(new_nums)):
            while right < len(new_nums) and new_nums[right] < new_nums[left] + nums_len:
                right += 1

                count = right - left
                ops = min(ops, nums_len - count)

        return ops

