class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # transpose
        rows = len(matrix)
        cols = len(matrix[0])


        for i in range(rows):
            for j in range(i + 1, cols):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


        for row in matrix:
            self.reverse(row)




    def reverse(self,row):
        
        left = 0
        right = len(row) - 1


        while left <= right:
            row[left], row[right] = row[right], row[left]

            left+=1
            right -= 1
