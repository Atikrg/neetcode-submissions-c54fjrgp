class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for character in s:
            if character == "[":
                res.append("]")

            elif character == "(":
                res.append(")")

            elif character == "{":
                res.append("}")

            elif len(res) == 0 or  res.pop() != character:
                return False

        return len(res) == 0