# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        res = []
        while queue:
            right = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right = node
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
            if right:
                res.append(right.val)
        return res
if __name__=="__main__":
    '''
        EXPECTED OUTPUT:
            Input: root = [1,2,3,null,5,null,4]
            Output: [1,3,4]
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left = None
    obj = Solution()
    ans = obj.rightSideView(root= root)
    print(ans)  