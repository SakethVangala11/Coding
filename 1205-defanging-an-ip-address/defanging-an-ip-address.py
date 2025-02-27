class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ""
        n = len(address)
        for i in range(n):
            if address[i]==".":
                s+="[.]"
            else:
                s+=address[i]
        return s
        