class Solution:
    def palindrome(self,word):
            i=0
            j=len(word)-1
            while(i<=j):
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.palindrome(word):
                return word
        return ""


        