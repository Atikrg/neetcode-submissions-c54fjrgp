class Solution:
    def reverse(self, x: int) -> int:



        positive = False


        if x > 0:
            positive = True


        number = abs(x)

        newNum = 0
        while number > 0:
            digit = number % 10
            newNum = newNum * 10 + digit

            number = number // 10


        sign = -1 if x < 0 else 1

        newNum *= sign


        if newNum < (-1 << 31) or newNum > (1 << 31) -1:
            return 0

        return newNum
