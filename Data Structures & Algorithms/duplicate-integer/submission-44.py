class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        hashMap = {}

        for i in nums:
            if i in hashMap:
                return True
            hashMap[i]= True
        return False
