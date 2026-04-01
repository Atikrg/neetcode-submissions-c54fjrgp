class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        uniqueElements = set()
        for i in range(len(nums)):
            if nums[i] in uniqueElements:
                return True

            element = nums[i]
            uniqueElements.add(element)

        return False