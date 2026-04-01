class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return 

        first_row = first_col = False
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True

                    if j == 0:
                        first_col = True

                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col:
            for i in range(rows):
                matrix[i][0] = 0