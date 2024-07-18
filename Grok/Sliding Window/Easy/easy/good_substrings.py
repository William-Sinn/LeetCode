class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 2
        good = 0

        while end < len(s):
            if s[start] != s[start + 1] and s[start] != s[end] and s[start + 1] != s[end]:
                good += 1
            
            start += 1
            end += 1

        return good