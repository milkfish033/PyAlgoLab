#https://leetcode.cn/problems/diameter-of-binary-tree/submissions/644633259/?envType=study-plan-v2&envId=top-100-liked
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans  = 0
        def dfs(node):
            if node is None:
                return -1
            
            l = dfs(node.left) + 1
            r = dfs(node.right) + 1
            nonlocal ans
            ans = max(ans , l + r)
            return max(l, r)

        dfs(root)
        return ans 