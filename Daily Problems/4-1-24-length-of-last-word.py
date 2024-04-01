class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0

        for c in range(len(s) - 1, 0, -1):

            if s[c] == " ":
                if l > 0:
                    break
            else:
                l += 1

        return l
