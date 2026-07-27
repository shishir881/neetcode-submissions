class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0]) if r > 0 else 0
        front=0
        back=r*c-1
        while front<=back:
            middle=(front+back)//2
            i=middle//c
            j=middle%c
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                front=i*c+j+1
            else:
                back=i*c+j-1
        return False



        