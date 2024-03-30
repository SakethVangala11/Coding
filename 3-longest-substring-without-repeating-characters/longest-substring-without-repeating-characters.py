class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Optimal Solution - O(n) -  Sliding Window
        l = 0 
        maxi = 0
        i, j = 0, 0
        n = len(s)
        ele = set()
        while(j<n):
            if s[j] not in ele:
                ele.add(s[j])
                l = j-i+1
                maxi = max(maxi, l)
            else:
                while(s[i]!=s[j]):
                    ele.remove(s[i])
                    i+=1
                i+=1
                ele.add(s[j])
                l = j-i+1
                maxi = max(maxi, l)
            j+=1
        return maxi