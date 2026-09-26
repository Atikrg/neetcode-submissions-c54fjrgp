class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        def helper(x, n):

            if x == 0:
                return 0

            if n == 0:
                return 1


            result = helper(x, n // 2)

            result *= result


            return x * result if n % 2 else result


        result = helper(x, abs(n))


        return result if n >= 0 else 1 / result



# helper(2, 5) => 4 * 4 => 16 * 2 => 32
# helper(2, 2)=>  2 * 2 => 4 * 2 => 4
# helper(2, 1) => 1 * 1 => 1 * 2 => 2