class Solution:

    def sumOfSquares(self, n):
        total = 0

        while n:
            digit = n % 10
            total += (digit ** 2)
            n = n // 10

        return total

    def isHappy(self, n: int) -> bool:
        
        visit = set()


        while n not in visit:
            visit.add(n)

            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False
