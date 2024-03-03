class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        license = ""
        for i in s:
            if i == "-":
                pass
            else:
                license+=i
        ans  = ""
        count = 0
        for i in range(len(license)-1,-1,-1):
            if count == k:
                ans+="-"
                count=0
            ans+= license[i]
            count+=1
        return ans[::-1].upper()


        