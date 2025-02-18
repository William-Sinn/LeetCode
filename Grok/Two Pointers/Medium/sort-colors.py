class Solution:
    def sortColors(self, nums):
        left = right = 0
        colors = [0, 0, 0]

        while right < len(nums):
            colors[nums[right]] += 1
            right += 1
        
        while left < len(nums):
            if colors[0] > 0:
                nums[left] = 0
                colors[0] -= 1
            elif colors[1] > 0:
                nums[left] = 1
                colors[1] -= 1
            else:
                nums[left] = 2
            left += 1
