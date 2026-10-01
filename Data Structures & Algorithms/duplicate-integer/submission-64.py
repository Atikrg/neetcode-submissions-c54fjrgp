class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False


        mpp = Counter(nums)

        for key, value in mpp.items():
            if value >= 2:
                return True

        return False