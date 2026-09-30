class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = re.sub(r'[^A-za-z0-9]', '', s.lower())

        print(string)


        left = 0
        right = len(string) - 1


        while left < right:

            if string[left] != string[right]:
                return False


            left +=1
            right -= 1

        return True
