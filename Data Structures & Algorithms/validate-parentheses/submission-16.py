class Solution:
    def isValid(self, s: str) -> bool:
        
        res = []
        for char in s:
            if char == "[":
                res.append("]")

            elif(char == "("):
                res.append(")")

            elif(char == "{"):
                res.append("}")

            elif(len(res) == 0 or res.pop() != char):
                return False

        return len(res) == 0
        
