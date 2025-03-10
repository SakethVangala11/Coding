class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for i in range(n):
            for j in range(n):
                if baskets[j]!=-1 and baskets[j] >= fruits[i]:
                    baskets[j] = -1
                    break
        count =0
        for i in range(n):
            if baskets[i]!=-1:
                count+=1
        return count
                
        