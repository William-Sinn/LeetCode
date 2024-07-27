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
        sec_path = left_path
        left = [startPos]
        right = [startPos]
        prim_dir = right
        sec_dir = left
        i = 1

        for fruit in fruits:
            if fruit[0] > startPos:
                if fruit[0] <= startPos + k:
                    right_path[fruit[0]] = fruit[1]
                    right_pre += fruit[1]

            elif fruit[0] == startPos:
                max_fruits += fruit[1]

            else:
                if fruit[0] >= startPos - k:
                    left_path[fruit[0]] = fruit[1]
                    left_pre += fruit[1]

        if left_pre > right_pre:
            path = left_path
            sec_path = right_path
            prim_dir = left
            sec_dir = right
            i = -1

        if (len(right_path) or len(left_path)):
            while abs(left[0] - right[0]) < k and prim_dir[0] >= 0:
                prim_dir[0] += i
                if prim_dir[0] in path:
                    max_fruits += path[prim_dir[0]]

            curr_fruits = max_fruits

            if prim_dir[0] in path:
                curr_fruits -= path[prim_dir[0]]

            while prim_dir[0] != startPos and sec_dir[0] >= 0:
                prim_dir[0] += -i
                if prim_dir[0] in path:
                    curr_fruits -= path[prim_dir[0]]

                sec_dir[0] += -i
                if sec_dir[0] in sec_path:
                    curr_fruits += sec_path[sec_dir[0]]
                
                max_fruits = max(max_fruits, curr_fruits)


        return max_fruits