class Solution(object):
    def lengthOfLongestSubstring(self, s):
        len_s = len(s)
        o = 0
        left = 0
        right = 0
        char_dict = {}
        c = 0

        while right < len_s:

            if s[right] not in char_dict:
                c += 1
                o = max(o, c)
                char_dict[s[right]] = 1
                right += 1
            
            else:
                while s[right] in char_dict:
                    del char_dict[s[left]]
                    left += 1
                    c -= 1
        
        return o

