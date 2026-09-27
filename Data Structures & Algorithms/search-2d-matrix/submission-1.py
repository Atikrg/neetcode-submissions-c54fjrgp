class Solution:


    def binarySearch(self, row, target):


        left = 0
        right = len(row) - 1



        while left <= right:

            mid = (left + right) //2


            if row[mid] == target:
                return True

            if target < row[mid]:
                right = mid - 1

            elif target > row[mid]:
                left = mid + 1




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if self.binarySearch(row, target):
                return True

        return False