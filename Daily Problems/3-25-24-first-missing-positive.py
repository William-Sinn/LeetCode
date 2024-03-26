class Solution(object):
    def firstMissingPositive(self, nums):

        min_num = 1
        num_dict = {}

        for num in nums:

            if num not in num_dict:
                num_dict[num] = num

            if num == min_num & num > 0:

                while min_num in num_dict:
                    min_num += 1
        
        return min_num