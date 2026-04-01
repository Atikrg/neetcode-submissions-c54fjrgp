/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} subRoot
     * @return {boolean}
     */

    
       preOrderTraversal(node) {
        if (node === null) {
            return null;
        }

        let result = node.val.toString();
        result += this.preOrderTraversal(node.left);
        result += this.preOrderTraversal(node.right);

        return result;
    }

    isSubtree(root, subRoot) {
        const fullTree = this.preOrderTraversal(root);
        const subTree = this.preOrderTraversal(subRoot);

        return fullTree.includes(subTree);
    }
}
