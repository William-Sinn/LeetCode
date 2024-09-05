class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        p2 = 0
        p3 = float('inf')
        ans = []
        s_len = len(s)

        for p1 in range(s_len):
            while p2 < s_len - 1 and s[p2] != c:
                p2 += 1

            if s[p2] == c:
                ans.append(min(abs(p1 - p2), abs(p1 - p3)))
            else:
                ans.append(abs(p1 - p3))

            if p2 == p1:
                p3 = p1
                p2 += 1
                        
        return ans