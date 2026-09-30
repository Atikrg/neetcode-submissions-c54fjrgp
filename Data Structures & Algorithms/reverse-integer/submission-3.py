class Solution:
    def reverse(self, x: int) -> int:
        


        number = abs(x)
        reverse = 0
    
        while number > 0: 
            digit = number % 10
            reverse = reverse * 10 + digit
            number = number // 10


        if x < 0:
            reverse  = -reverse


        if reverse < (-1 << 31) or reverse > (1 << 31) -1:
            return 0

        return reverse