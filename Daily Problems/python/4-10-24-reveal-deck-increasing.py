from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        d_len = len(deck)
        out_deck = [None] * d_len
        index_arr = deque(range(d_len))

        for card in sorted(deck):
            out_deck[index_arr.popleft()] = card

            if index_arr:
                index_arr.append(index_arr.popleft())
        
        return out_deck
