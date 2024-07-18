class Solution(object):
    def countSubarrays(self, nums, k):
        left = 0
        right = 0 
        max_num = max(nums)
        max_count = 0
        arr_len = len(nums)
        out = 0

        while right < arr_len:
            if nums[right] == max_num:
                max_count += 1

            while max_count >= k:
                if nums[left] == max_num:
                    max_count -= 1
                out += arr_len - right
                left += 1
            
            right += 1
        
        return out