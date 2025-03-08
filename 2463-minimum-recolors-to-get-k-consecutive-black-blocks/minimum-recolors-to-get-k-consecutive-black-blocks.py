class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        w = 0
        for i in range(0,k):
            if blocks[i]=="W":
                w+=1
        i, j = 0, k
        mini = w
        while(j<n):
            if blocks[j] == "W":
                w+=1
            if blocks[i] == "W":
                w-=1
            i+=1
            j+=1
            mini = min(mini, w)
        return mini
            








        