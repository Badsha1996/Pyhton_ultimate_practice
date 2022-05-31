# Binary tree has two node 
# there are also 1. perfect bt : all nodes complete
# 2. degenerate bt : only have one child for each node
# 3. complete bt : perfect tree except last nodes(possible left)
# 4. balanced bt : at least 1 node gap allowed between left and right

# Operation for binary tree
# insertion : O(h)
# deletion :  O(h)
# search :    O(h)
from collections import deque



class TreeNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self,root=None) -> None:
        self.root = TreeNode(root)
    def insert(self, element) -> None:
        # create a new tree node 
        node = TreeNode(element)
        if not self.root:
            self.root = node
            return 
        queue = deque([self.root])
        while queue:
            treeNode = queue[0]
            if not treeNode.left:
                treeNode.left = node
                break
            else:
                queue.appendleft(treeNode.left)
            if not treeNode.right:
                treeNode.right = node
                break
            else:
                queue.appendleft(treeNode.right)
    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        print(root.data,  end = "->")
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return 
        print(root.data,  end = "->")
        self.preorder(root.left)
        self.preorder(root.right) 

    def postorder(self, root):
        if not root:
            return 
        self.postorder(root.left)
        self.postorder(root.right) 
        print(root.data,  end = "->")
    def levelorder(self, root):
        if not root:
            return 
        queue = deque([root])
        while queue:
            Qlen = len(queue)
            for _ in range(Qlen):
                node = queue.pop()
                print(node.data)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)  
            print("---------------")  

    def printTree(self) -> None:
        if not self.root:
            print("The tree is empty")
            return 
        root = self.root
        queue = deque([root])
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(node.data, end=" -> ")
        
if __name__=="__main__":
    tree = BinaryTree(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.printTree()
    print("")
    tree.inorder(tree.root)
    print("")
    tree.preorder(tree.root)
    print("")
    tree.postorder(tree.root)
    print("")
    tree.levelorder(tree.root)
    