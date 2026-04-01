class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None  # Break the first half

        l1 = head
        l2 = self.reverse(slow)  # Reverse the second half

        self.merge(l1, l2)  # Merge two halves

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def merge(self, l1: ListNode, l2: Optional[ListNode]):
        while l2:
            nextNode = l1.next
            l1.next = l2
            l1 = l2
            l2 = nextNode