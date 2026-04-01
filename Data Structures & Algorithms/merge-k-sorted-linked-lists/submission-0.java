/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // Min-heap to prioritize nodes based on their values
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);

        // Add all the head nodes of the k lists to the priority queue
        for (ListNode node : lists) {
            if (node != null) {
                pq.offer(node);
            }
        }

        // Dummy node to start the merged list
        ListNode dummyNode = new ListNode(-1);
        ListNode temp = dummyNode;

        // Process nodes from the priority queue
        while (!pq.isEmpty()) {
            // Get the node with the smallest value
            ListNode minNode = pq.poll();

            // Add the next node in the list to the queue if it exists
            if (minNode.next != null) {
                pq.offer(minNode.next);
            }

            // Attach the smallest node to the merged list
            temp.next = minNode;
            temp = temp.next;
        }

        // Return the head of the merged list (next node after the dummy node)
        return dummyNode.next;
    }
}
