from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

# Solution 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # I have done recursive inorder traversal(binaryTree/concepts folder) 
        # so here i wanna do iterative and morris traversal approch 
        # Morris traversal 
        if not root:
            return []
        res = []
        cur = root
        pre = None
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur
                nxt = cur.left
                cur.left = None
                cur = nxt
        return res



if __name__=="__main__":
    '''
        EXPECTED OUTPUT:
            Input: root = [1,null,2,3]
            Output: [1,3,2]
    '''
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    obj = Solution()
    print(obj.inorderTraversal(root=root))
    
