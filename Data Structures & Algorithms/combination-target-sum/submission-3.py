class Solution:
    
    def helper(self, candidates, target, path, result, i):

        if target == 0:
            result.append(path.copy())
            return

        if i >= len(candidates) or target < 0:
            return

        # take current number
        path.append(candidates[i])
        self.helper(candidates, target - candidates[i], path, result, i)
        path.pop()

        # skip current number
        self.helper(candidates, target, path, result, i + 1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.helper(candidates, target, [], result, 0)
        return result