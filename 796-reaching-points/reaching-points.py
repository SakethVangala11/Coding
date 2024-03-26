class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        if sx == tx:
            return (ty-sy)%sx == 0
        if sy == ty:
            return (tx-sx)%ty == 0
        if ty > tx:
            return self.reachingPoints(sx, sy, tx, ty%tx)
        if tx > ty:
            return self.reachingPoints(sx, sy, tx%ty, ty)
        return False
        


        

        