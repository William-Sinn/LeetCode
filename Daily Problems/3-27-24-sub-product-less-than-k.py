class Solution(object):

    valid_subs = 0

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start_i = 0
        end_i = 0
        arr_len = len(nums)

        p = 1
        while start_i < arr_len:
            p *= nums[end_i]

            if p >= k: 
                p = p/nums[end_i]

                if start_i == end_i:
                    end_i += 1
                    start_i += 1
                    continue


                if p < k:
                    self.valid_subs += end_i - start_i
                    p = p/nums[start_i]
                
                    
                start_i +=1



            elif end_i + 1 == arr_len:

                p = p/nums[start_i]

                if p < k:
                    self.valid_subs += end_i + 1 - start_i
                    
                start_i +=1
            
                p = p/nums[end_i]

            else:
                end_i += 1

            


        return self.valid_subs