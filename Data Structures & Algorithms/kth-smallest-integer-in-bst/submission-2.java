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

    private TreeNode helper(TreeNode root, int k, int[] counter) {
        if (root == null) {
            return null;
        }

        TreeNode node = helper(root.left, k, counter); // Traverse the left subtree
        if (node != null) return node;

        counter[0]++; // Increment the counter when visiting a node
        if (counter[0] == k) return root;

        return helper(root.right, k, counter); // Traverse the right subtree
    }

    public int kthSmallest(TreeNode root, int k) {
        int[] counter = new int[1]; // Array to hold the counter reference
        TreeNode node = helper(root, k, counter);
        return node != null ? node.val : -1; 
    }
}
