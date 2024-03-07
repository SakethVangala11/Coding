class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sr = ""
        tr =""
        def modify(original,modified):
            for i in original:
                if i== "#":
                    if modified:
                        modified =  modified[:-1:]
                else:
                    modified+=i
            return modified

        
        return modify(s,sr) == modify(t,tr)
        