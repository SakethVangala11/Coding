class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l = min(len(s1),len(s2),len(s3))
        count = 0
        print(l)
        for i in range(l):
            if s1[i]==s2[i] and s1[i]== s3[i] and s2[i]==s3[i]:
                count+=1
            else:
                break
        if count:
            return len(s1) + len(s2) + len(s3) - 3*count
        return -1






        