from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0]
        mono_stack = deque()
        ans = float("inf")

        for num in nums:
            prefix.append(prefix[-1] + num)

        print(prefix)

        for right in range(len(prefix)):
            print(mono_stack)
            while mono_stack and prefix[right] <= prefix[mono_stack[-1]]:
                mono_stack.pop()

            if mono_stack:
                print(prefix[right], prefix[mono_stack[0]])
            while mono_stack and prefix[right] - prefix[mono_stack[0]] >= k:
                print(ans, prefix[right], prefix[mono_stack[0]])
                ans = min(ans, right - mono_stack.popleft())
                print(mono_stack)
            
            mono_stack.append(right)
        
        return ans if ans != float("inf") else -1