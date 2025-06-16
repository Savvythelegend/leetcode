class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        """
        transpose elements across the diagonal elements
        """
        # Step 1: Transpose the matrix (swap elements across the diagonal)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #step 2: reverse each row of the matrix
        for i in range(n):
            matrix[i].reverse()