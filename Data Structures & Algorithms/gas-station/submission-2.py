class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        start = 0

        totalCost = 0
        totalGas = 0


        currentGas = 0

        for i in range(len(gas)):
            totalGas += gas[i];
            totalCost += cost[i]
            currentGas = currentGas + gas[i] - cost[i]

   
            if currentGas < 0:
                start = i + 1;
                currentGas = 0

        return -1 if totalGas < totalCost else start