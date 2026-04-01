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
     * @return {number}
     */
    maxDepth(root) {

        if(root == null)
        {
            return 0;
        }

        const queue = [];
        queue.push(root);
        let levels = 0;

        while(queue.length > 0)
        {
            levels++;
            const size = queue.length;
            
            for(let i = 0; i < size; i++)
            {
            const poppedNode = queue.shift();
            if(poppedNode.left != null) queue.push(poppedNode.left);
            if(poppedNode.right != null) queue.push(poppedNode.right);

            }


        }

        return levels;
    }
}
