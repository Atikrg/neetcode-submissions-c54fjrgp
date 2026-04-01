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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {

        const queue = [];

        queue.push(p);
        queue.push(q);


        while(queue.length > 0)
        {
            const first = queue.shift();
            const second = queue.shift();


            if(first == null && second == null )
            {
                continue;
            }else{
                if(first == null || second == null || first.val != second.val)
                {
                    return false;
                }
            }


            queue.push(first.left);
            queue.push(second.left);


            queue.push(first.right);
            queue.push(second.right);
        }

        return true;

    }
}
