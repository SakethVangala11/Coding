class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for i in paths:
            s.add(i[0])
            s.add(i[1])
        
        source = False
        destination = False

        for i in s:
            for j in paths:
                if i == j[0]:
                    source = True
                if i == j[1]:
                    destination = True

            if destination and not source:
                return i
            source = False
            destination = False


        