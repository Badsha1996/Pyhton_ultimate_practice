
# Set Matrix Zeroes
# leetcode - 73 
# Algorihtm :
        # use first row and coloum as tracker 
        # if encounter any 0 just set both first row and coloum to zero 
        # loop throuh the first row and col and set zero accordingly 
        # Time Complexity - O(n^2)
        # Space Complexity - O(1)


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        Rows = len(matrix)
        Cols = len(matrix[0])
        
        first_row = False
        
        # setting the frist row and col to zeros
        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 
                    if r==0:
                        first_row = True
                    else:
                        matrix[r][0] = 0
        
        
        # loop through rest of the matrix
        for r in range(1, Rows):
            for c in range(1, Cols):
                if matrix[0][c]==0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # if mat[0][0] == 0
        if matrix[0][0] == 0:
            for r in range(Rows):
                matrix[r][0] = 0
                
        # if flag == true
        if first_row == True:
            for  c in range(Cols):
                matrix[0][c] = 0

if __name__ == "__main__":

    '''
        Expected - 
        Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Output: [[1,0,1],[0,0,0],[1,0,1]]
    '''
    obj = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    obj.setZeroes(matrix)
    print(matrix)

