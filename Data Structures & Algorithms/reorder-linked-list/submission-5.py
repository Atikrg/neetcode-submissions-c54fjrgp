# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        l1 = head
        l2 = self.reverseList(slow)

        self.merge(l1, l2)

    def merge(self, l1, l2):

        while l2:
            nextNode = l1.next
            l1.next = l2
            l1 = l2
            l2 = nextNode

    def reverseList(self, head):
        prevNode = None
        currentNode = head


        while (currentNode != None):
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        return prevNode