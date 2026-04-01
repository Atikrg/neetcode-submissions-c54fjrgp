import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Needed so heapq can compare ListNode objects
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        min_heap = []

        # push head of each list
        for node in lists:
            if node:
                heapq.heappush(min_heap, node)

        dummy = ListNode(-1)
        curr = dummy

        while min_heap:
            node = heapq.heappop(min_heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, node.next)

        return dummy.next
