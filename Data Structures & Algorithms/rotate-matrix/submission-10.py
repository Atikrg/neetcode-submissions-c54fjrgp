class Solution:
    def reverse(self, row):
        left = 0
        right = len(row) - 1

        while left < right:
            row[left], row[right] = row[right], row[left]

            left += 1
            right -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])

        # Transpose
        for i in range(rows):
            for j in range(i + 1, columns):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row
        for i in range(rows):
            self.reverse(matrix[i])