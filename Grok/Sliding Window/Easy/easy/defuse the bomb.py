class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = []
        n = len(code)

        step = 1
        if k < 0:
            step = -1
        start = 0
        end = k

        while len(out) < n:
            int_sum = 0

            for x in range((start + step), (end + step), step):
                int_sum += code[int(x % n)]

            out.append(int_sum)

            start += 1
            end += 1

        
        return out
                
            