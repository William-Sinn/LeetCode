class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"
        
        mono_inc = []
        for i, n in enumerate(num):
            if not mono_inc or n >= mono_inc[-1]:
                mono_inc.append(n)
            else:
                while mono_inc and n < mono_inc[-1]:
                    mono_inc.pop()
                    k -= 1
                    if k == 0:
                        res = ''.join(mono_inc)+num[i:]
                        while len(res)>1 and res[0] == '0':
                            res = res[1:]
                        return res
                mono_inc.append(n)   
                
        res = ''.join(mono_inc[:-k])
        while len(res)>1 and res[0] == '0':
            res = res[1:]
        return res