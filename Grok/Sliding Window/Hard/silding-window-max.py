from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        left = 0
        right = 0
        max_win = []
        dq= deque()

        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)
        
            if right + 1 - left == k:
                max_win.append(nums[dq[0]])

                if nums[left] == nums[dq[0]]:
                    dq.popleft()
                
                left += 1

            right += 1

        return max_win