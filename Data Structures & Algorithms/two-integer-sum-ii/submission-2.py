from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            # Starting point
            total = numbers[left] + numbers[right]

            # Found the target
            if total == target:
                return [left + 1, right + 1]

            # Need a bigger sum
            elif total < target:
                left += 1

            # Need a smaller sum
            else:
                right -= 1

        return [-1, -1]