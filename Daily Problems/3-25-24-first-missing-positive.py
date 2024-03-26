class Solution(object):
    def firstMissingPositive(self, nums):
        num_length = len(nums)

        for num in nums:
            index = num - 1
            if index >= 0 and index < num_length:
                int_index = int(index)
                nums[int_index] = float(nums[int_index])

        for i in range(num_length):
            if isinstance(nums[i], int):
                return i + 1

        return num_length + 1