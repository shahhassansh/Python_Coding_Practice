class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def postOrderTraversal(root):
    if root != None:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
postOrderTraversal(root)