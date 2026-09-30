class Solution:
    def maxDepth(self, s: str) -> int:
        

        stack = []
        answer = 0
        for i in s:


            answer = max(answer, len(stack))
            if i == ")":
                stack.pop()

            elif(i == "("):
                stack.append("(")

        return answer




