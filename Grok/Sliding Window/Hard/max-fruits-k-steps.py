from copy import deepcopy
class Solution(object):
    def pathTraverse(self, path, sec_path, prim_dir, sec_dir, i, startPos, k, max_fruits):
        while abs(prim_dir - sec_dir) < k:
            prim_dir += i
            if prim_dir in path:
                max_fruits += path[prim_dir]
        curr_fruits = max_fruits
        if prim_dir in path:
            curr_fruits -= path[prim_dir]
        while abs(sec_dir - startPos) <= k/2 and sec_dir >= 0:
            if sec_dir != startPos:
                prim_dir += -i
                if prim_dir in path:
                    curr_fruits -= path[prim_dir]
            prim_dir += -i
            if prim_dir in path:
                curr_fruits -= path[prim_dir]
            sec_dir += -i
            if sec_dir in sec_path:
                curr_fruits += sec_path[sec_dir]
                del sec_path[sec_dir]
            max_fruits = max(max_fruits, curr_fruits)
        return max_fruits

    def maxTotalFruits(self, fruits, startPos, k):
        max_fruits = 0
        right_path = {}
        left_path = {}
        right_pre = 0
        left_pre = 0
        left = startPos
        right = startPos
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
        if (len(right_path) or len(left_path)):
            right_max = (self.pathTraverse(right_path, deepcopy(left_path), right, left, 1, startPos, k, max_fruits))
            left = startPos
            right = startPos
            left_max = (self.pathTraverse(left_path, right_path, left, right, -1, startPos, k, max_fruits))
            max_fruits = max(left_max, right_max)
        return max_fruits