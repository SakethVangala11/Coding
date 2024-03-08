class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        maxi = 0
        for i in nums:
            if i in freq:
                freq[i] += 1
                if freq[i] > maxi:
                    maxi = freq[i]
            else:
                freq[i] = 1
                if freq[i] > maxi:
                    maxi = freq[i]
        count = 0
        for i in freq:
            if freq[i]==maxi:
                count+=1
        return count*maxi

        