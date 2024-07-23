class Solution(object):
    def checkInclusion(self, s1, s2):
        s1_dict = {}
        s2_dict = {}
        left = 0
        right = 0
        s1_len = len(s1)

        for c in s1:
            if c in s1_dict:
                s1_dict[c] += 1
            else:
                s1_dict[c] = 1

        while right < len(s2):
            if s2[right] in s2_dict:
                s2_dict[s2[right]] += 1

            else:
                s2_dict[s2[right]] = 1

            if right + 1 - left < s1_len:
                right += 1
            
            else: 
                if s1_dict == s2_dict:
                    return True
                
                right += 1
                if s2_dict[s2[left]] == 1:
                    del s2_dict[s2[left]]
                else: 
                    s2_dict[s2[left]] -= 1
                left += 1
        
        return False