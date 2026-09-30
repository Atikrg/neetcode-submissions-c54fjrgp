class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = Counter(hand)


        minHeap = list(count.keys())

        heapq.heapify(minHeap)


        while minHeap:
            first = minHeap[0]

            for j in range(first, first + groupSize):
                if j not in count:
                    return False
                count[j] -= 1

                if count[j] == 0:
                    heapq.heappop(minHeap)


        return True