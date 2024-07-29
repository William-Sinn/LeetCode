from heapq import heappush, heappop

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        num_heap = []
        win_size = float('inf')
        pref_array = []
        pref_sum = 0
        num_dict = {}

        i = 0
        for num in nums:
            heappush(num_heap, -num)

            pref_sum += num
            pref_array.append(pref_sum)

            num_dict[num] = i
            i += 1
        
        if pref_array[-1] < k:
            return -1
        elif pref_array == k:
            return len(nums) 

        while len(num_heap):
            sum = 0
            num = -heappop(num_heap)
            curr_win = 1
            left = right = num_dict[num]
            pref_left = 0
            pref_right = 0

            while sum < k:
                if curr_win >= win_size:
                    break

                if left -1 < 0 or 

