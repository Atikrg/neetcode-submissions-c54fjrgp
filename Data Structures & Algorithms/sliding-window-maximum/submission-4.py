class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      
      queue = deque()

      result = []

      left = 0
      for i in range(len(nums)):

        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()


        queue.append(i)

        left = i - k + 1

        if queue[0] < left:
          queue.popleft()


        if i >= k - 1:
          result.append(nums[queue[0]])

      return result