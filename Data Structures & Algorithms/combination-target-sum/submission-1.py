class Solution:


    def __init__(self):
        self.s = set()


    def getAllCombinations(self,index, answer, target, nums, combination):
        

        if index == len(nums) or target < 0:
            return


        if target == 0:
            if tuple(combination) not in self.s:
                answer.append(list(combination))
                self.s.add(tuple(combination))
            return;

        combination.append(nums[index])

        #single
        self.getAllCombinations(index + 1, answer, target - nums[index], nums,combination)
        

        #multiple
        self.getAllCombinations(index, answer, target - nums[index], nums, combination)

        combination.pop()

        self.getAllCombinations(index + 1, answer, target,nums, combination)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        combination = []

        self.getAllCombinations(0,answer,target, nums ,combination)

        return answer
        
