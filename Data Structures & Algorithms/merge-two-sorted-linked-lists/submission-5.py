# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()  # Create a dummy node
        tail = dummyNode  # Tail pointer to build the merged list

        while list1 and list2:  # Traverse both lists
            if list1.val <= list2.val:  # Pick the smaller node
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the tail pointer forward

        # Append the remaining nodes of whichever list is not empty
        tail.next = list1 if list1 is not None else list2

        return dummyNode.next  # Return the merged list starting from the next of dummyNode