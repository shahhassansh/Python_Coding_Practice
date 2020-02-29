class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def inOrderTraversal(root):
    if root != None:
        inOrderTraversal(root.left)
        print(root.val)
        inOrderTraversal(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inOrderTraversal(root))

