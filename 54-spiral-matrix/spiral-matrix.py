class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res  = []

        while(left<right and top<bottom):

            #Add elements from left to right in top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1

            #Add elements from top to bottom in right-most row
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1

            #For column matrix or row matrix or if one row or column in sub problems
            if not(left<right and top<bottom):
                break
            
            #Add elements from right to left in bottom-most row
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            
            #Add elements from bottom to top in left row
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        
        return res