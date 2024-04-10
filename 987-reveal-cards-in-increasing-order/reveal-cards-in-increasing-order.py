from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque([])
        deck.sort()
        for i in range(len(deck)-1,-1,-1):
            if d:
                x = d.pop()
                d.appendleft(x)
                d.appendleft(deck[i])
            else:
                d.append(deck[i])
        return d

        
        