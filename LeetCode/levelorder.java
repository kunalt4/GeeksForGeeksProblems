/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null)
            return res;
        Queue<TreeNode> que = new LinkedList<TreeNode>();
        
        que.add(root);
        while(!que.isEmpty()){
            List<Integer> level = new ArrayList<>();
            int cnt = que.size();
            for(int i=0;i<cnt;i++){
                TreeNode node = que.poll();
                level.add(node.val);
                if(node.left!=null)
                    que.add(node.left);
                if(node.right!=null)
                    que.add(node.right);
            }
            res.add(level);
        }
        return res;
        
    }
}