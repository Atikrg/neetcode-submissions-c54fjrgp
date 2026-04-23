class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        

        if not matrix:
            return;

        firstRow = False
        firstCol = False


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:    
                    if i == 0:
                        firstRow = True
                    
                    if j == 0:
                        firstCol = True

                    matrix[0][j] = 0
                    matrix[i][0] = 0



        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0


        if firstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if firstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0