class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        start_p = 0
        max_length = 0
        max_freq = 0  # Track the maximum frequency

        for end_p, num in enumerate(nums):
            freq[num] += 1
            max_freq = max(max_freq, freq[num])  # Update max_freq

            while max_freq > k:
                freq[nums[start_p]] -= 1
                if freq[nums[start_p]] == 0:
                    del freq[nums[start_p]]
                start_p += 1

                # Recalculate max_freq
                if freq:  # Check if freq is not empty
                    max_freq = max(freq.values())

            # Update max_length outside the while loop
            max_length = max(max_length, end_p - start_p + 1)

        return max_length
