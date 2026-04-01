class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        longest = 0

        for i in range(len(nums)):
            currentNum = nums[i]
            currentStreak = 1


            while currentNum + 1 in nums:
                currentNum +=1
                currentStreak += 1

            longest = max(currentStreak, longest)


        return longest
            

            
    