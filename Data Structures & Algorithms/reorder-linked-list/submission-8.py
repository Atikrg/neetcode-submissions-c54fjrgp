# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return


        slow = head

        fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        slow.next = None


        prev = None
        currentNode = second


        while currentNode  != None:
            nextNode = currentNode.next
            currentNode.next = prev


            prev = currentNode


            currentNode = nextNode

        
        second = prev

        first = head


        while second: 
            first_next = first.next
            second_next = second.next


            first.next = second

            second.next = first_next


            first = first_next

            second = second_next
