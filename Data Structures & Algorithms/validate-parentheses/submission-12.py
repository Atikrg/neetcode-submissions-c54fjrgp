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


            elif len(stack) == 0 or stack.pop() != character:
                return False

        return len(stack) == 0

            