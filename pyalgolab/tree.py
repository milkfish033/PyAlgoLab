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

    
#https://leetcode.cn/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-100-liked
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if  root is None:
            return []
        q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                n = q.popleft()
                tmp.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(tmp)
        return res 
        