class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        current = 0
        right = 0
        left = 0
        add = 0

        while right - left < minutes:
            if grumpy[right] == 1:
                current += customers[right]
            else:
                add += customers[right]
            right += 1
        
        out = current

        while right < len(customers):
            if grumpy[right] == 1:
                current += customers[right]
            else:
                add += customers[right]
            
            if grumpy[left] == 1:
                current -= customers[left]
            
            out = max(current, out)

            right += 1
            left += 1
        
        return out + add