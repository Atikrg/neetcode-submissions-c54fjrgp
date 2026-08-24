class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False


        mpp = {}


        for num in nums:
            mpp[num] = 1 + mpp.get(num, 0)


        for key, value in mpp.items():
            if value >= 2:
                return True

        return False