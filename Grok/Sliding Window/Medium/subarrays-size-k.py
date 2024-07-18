class Solution(object):
    def numOfSubarrays(self, arr, k, threshold): 
        start = 0
        end = 0
        total = 0
        out = 0

        while end < len(arr):
            total += arr[end]

            if end - start == k - 1:

                if total/k >= threshold:
                    out += 1
                    
                total -= arr[start]
                start += 1

            end += 1

        return out