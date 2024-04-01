class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        s_len = len(s) - 1

        for c in range(s_len + 1):

            if s[s_len - c] == " ":
                if l > 0:
                    break
            else:
                l += 1

        return l
