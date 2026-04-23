class Solution:

    def reverse(self,row):

        right = len(row) - 1
        left = 0


        while(left < right):


            row[right], row[left] = row[left], row[right]

            left +=1
            right -=1
        


    def rotate(self, matrix: List[List[int]]) -> None:

        if not matrix:
            return None
        
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(i +1,cols):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    
        for i in range(rows):

            row = matrix[i]

            self.reverse(row)

