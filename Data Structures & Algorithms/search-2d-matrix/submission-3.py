class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        i=0
        while i<ROWS:
            low,high=0,COLS-1
            if matrix[i][high]<target:
                i+=1
                continue
            while low<=high :
                mid=low+(high-low)//2
                if matrix[i][mid]==target:
                    return True
                if matrix[i][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            i+=1
        return False

