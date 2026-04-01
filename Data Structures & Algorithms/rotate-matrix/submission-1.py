
class Solution:
    
    def reverse(self, row: List[int]) -> None:
        left = 0
        right = len(row) - 1  # Fixing incorrect row length calculation

        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        
        # Transpose the matrix
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Reverse each row using self.reverse
        for i in range(len(matrix)):
            self.reverse(matrix[i])  # Correctly calling the method with self
