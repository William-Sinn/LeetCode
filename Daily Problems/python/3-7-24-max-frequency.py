class Solution(object):
    def maxFrequencyElements(self, nums):
        max_frq = 0
        total_frq = 0
        num_dict = {}

        for num in nums:

            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

            if num_dict[num] > max_frq:
                max_frq = num_dict[num]
                total_frq = 1
            elif num_dict[num] == max_frq:
                    total_frq += 1
        
        return(max_frq * total_frq)
