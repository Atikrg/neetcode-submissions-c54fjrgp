class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = set()

        for i in range(len(nums)):
            if nums[i] in mapp:
                return True
            mapp.add(nums[i])

        return False