class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        start = 0
        stop = 2
        o = 0
        n = len(colors)

        while start < n:
            if colors[start] == colors[stop % n] and colors[start] != colors[(start + 1) % n]:
                o += 1
            
            start += 1
            stop += 1
        
        return o