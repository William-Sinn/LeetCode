from collections import deque
class Solution(object):
    def __init__(self):
        self.ouset = set()
        self.addq = deque()
        self.kvalid = False
        self.avalid = True
        self.dict = {}
        self.block

    def reset(self):
        self.ouset = set()
        self.addq = deque()
        self.kvalid = False
        self.avalid = True
        self.dict = {}

    def addToTable(self, c, k):
        if c in self.dict:
            self.dict[c] += 1
        else:
            self.dict[c] = 1
        
        if self.dict[c] > k:
            self.ouset.add(c)
            self.kvalid = False
        elif self.dict[c] < k:
            self.ouset.add(c)
            self.kvalid = False
        elif self.dict[c] == k: 
            self.ouset.discard(c)
            if len(self.ouset) == 0: 
                self.kvalid = True
        
        self.addq.append(c)
        if len(self.addq) == 1 or abs(ord(self.addq[0]) - ord(self.addq[1])) <= 2:
            self.avalid = True
            self.addq.popleft()
        else:
            self.avalid = False

    def removeFromTable(self, c, k):
        if self.dict[c] - 1 == k:
            self.ouset.discard(c)
            if len(self.ouset) == 0:
                self.kvalid = True
        elif self.dict[c] - 1 == 0:
            print("discard C", c)
    
            self.ouset.discard(c)
            print("discard set", self.ouset)
            
            if len(self.ouset) == 0:
                self.kvalid = True
        elif self.dict[c] - 1 < k:
            self.ouset.add(c) 
            self.kvalid = False


        if self.dict[c] > 1:
            self.dict[c] -= 1
        else:
            del self.dict[c]

        if not self.avalid and self.addq[0] == c:
            self.addq.popleft()
            while len(self.addq) > 1 and abs(ord(self.addq[0]) - ord(self.addq[1])) <= 2:
                self.addq.popleft()
        
        if len(self.addq) == 0:
            self.avalid = True

    def subStringHelper(self, word, k):
        left = 0 
        right = 0
        out = 0

        while left < len(word):
            if right < len(word):
                self.addToTable(word[right], k)

            print("\n\n------------------------------")
            print(word[left:right+1])
            print(self.dict)
            print(left)
            print(right)
            print(out)
            print(self.ouset)
            print("k Valid", self.kvalid)
            print("a Valid", self.avalid)
            print("\n\n------------------------------")
            if right + 1 >= k and self.kvalid and self.avalid:
                out += 1
                
                while left <= right:
                    self.removeFromTable(word[left], k)
                    left += 1
            
            print(out)
            
            if right < len(word):
                right += 1
            elif left < len(word):
                self.removeFromTable(word[left], k)
                left += 1
                # if self.kvalid and self.avalid:
                #     out += 1
        return out  

    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        first = self.subStringHelper(word, k)


        return  (first*(first + 1))/2