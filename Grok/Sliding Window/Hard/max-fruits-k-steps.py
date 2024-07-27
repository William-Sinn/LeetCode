class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        max_fruits = 0
        curr_fruits = 0
        right_path = {}
        left_path = {}
        right_pre = 0
        left_pre = 0
        path = right_path
        left = startPos 
        right = startPos
        prim_dir = right
        sec_dir = left
        i = 1

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
            i = -1

        if (len(right_path) or len(left_path)):
            while abs(left - right) < k:
                prim_dir += i
                if prim_dir in path:
                    max_fruits += path[prim_dir]

            curr_fruits = max_fruits

            while prim_dir != startPos:
                if prim_dir in path:
                    curr_fruits -= path[prim_dir]
                prim_dir += -i

                sec_dir += -i
                if sec_dir in path:
                    curr_fruits += path[prim_dir]
                
                max_fruits = max(max_fruits, curr_fruits)

        return fruits