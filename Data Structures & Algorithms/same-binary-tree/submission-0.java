/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Queue to hold pairs of nodes for comparison
        Queue<TreeNode> queue = new LinkedList<>();

        // Add both root nodes to the queue for initial comparison
        queue.add(p);
        queue.add(q);

        while (!queue.isEmpty()) {
            // Poll two nodes at a time for comparison
            TreeNode first = queue.poll();
            TreeNode second = queue.poll();

            // Check if both nodes are null (both trees are identical up to this point)
            if (first == null && second == null) {
                continue; // Move to the next pair of nodes
            }

            // If one node is null or values don't match, trees are not the same
            if (first == null || second == null || first.val != second.val) {
                return false;
            }

            // Add the left children of both nodes to the queue
            queue.add(first.left);
            queue.add(second.left);

            // Add the right children of both nodes to the queue
            queue.add(first.right);
            queue.add(second.right);
        }

        // If we have compared all nodes and found no mismatches, the trees are identical
        return true;
    }
}
