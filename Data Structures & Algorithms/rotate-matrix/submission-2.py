class Solution:

    def reverse(self, row):
        left = 0 
        right = len(row) - 1

        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i + 1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            self.reverse(matrix[i])
