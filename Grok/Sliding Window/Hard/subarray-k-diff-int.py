class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.subarrayHelper(nums, k) - self.subarrayHelper(nums, k - 1)

    def subarrayHelper(self, nums, k):
        right = 0
        left = 0
        int_dict = {}
        count = 0
        out = 0


        while right < len(nums):
            if nums[right] in int_dict:
                int_dict[nums[right]] += 1
            else:
                int_dict[nums[right]] = 1
                count += 1
            
            while count > k:
                if int_dict[nums[left]] == 1:
                    del int_dict[nums[left]]
                    count -= 1
                else:
                    int_dict[nums[left]] -= 1

                left += 1
            
            out += right - left + 1
            right += 1

        return out