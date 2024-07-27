class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        fruits = 0
        right_path = {}
        left_path = {}
        right_pre = 0
        left_pre = 0
        path = right_path
        left = startPos 
        right = startPos
        prim_dir = right
        sec_dir = left

        for fruit in fruits:
            if fruit[0] > startPos:
                if fruit[0] <= startPos + k:
                    right_path[fruit[0]] = fruit[1]
                    right_pre += fruit[1]

            elif fruit[0] == startPos:
                fruits += fruits[1]

            else:
                if fruit[0] >= startPos - k:
                    left_path[fruit[0]] = fruit[1]
                    left_pre += fruit[1]

        if left_pre > right_pre:
            path = left_path
            prim_dir = left
            sec_dir = right

        if (len(right_path) or len(left_path)):
            while abs(left - right) < k:
                prim_dir += 1
                if prim_dir in path:
                    fruits += path[prim_dir]
            while abs


        return fruits