class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        if not gas or not cost:
            return 0


        if len(gas) > len(cost):
            return 

        
        totalGas = 0
        totalCost = 0

        start = 0

        next_requiredGas = 0

        for i in range(len(gas)):

            totalGas = totalGas + gas[i]
            totalCost = totalCost + cost[i]


            next_requiredGas = next_requiredGas + gas[i] - cost[i]

            if next_requiredGas < 0:
                start = i + 1

                next_requiredGas = 0


 

        return -1 if totalGas < totalCost else start