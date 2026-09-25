class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)

        cols = len(matrix[0])

        firstRow = False

        firstCol = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:

                    if i == 0:
                        firstRow = True


                    if j  == 0:
                        firstCol = True



                    matrix[i][0] = 0

                    matrix[0][j] = 0
                     


        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0


        if firstRow:
            for i in range(cols):
                matrix[0][i] = 0


        if firstCol:
            for j in range(rows):
                matrix[j][0] = 0




