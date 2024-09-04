class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        left = 0
        right = 0
        len_col = len(colors)
        out = 0
        while left < len_col:
            if right - left == k - 1:
                out += 1
                left += 1
            else:
                if colors[right%len_col] != colors[(right+1)%len_col]:
                    right += 1
                else:
                    left = right = right + 1
        return out