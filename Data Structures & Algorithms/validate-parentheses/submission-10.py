class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for character in s:
            if character == '[':
                stack.append(']')

            elif character == '{':
                stack.append('}')

            elif character == '(':
                stack.append(')')


            elif not stack or stack.pop() != character:
                return False

        return not stack

            