class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def preOrderTraversal(root):
    if root != None:
        #print(root.val)
        arr.append(root.val)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)
    return arr

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
arr = []
print(preOrderTraversal(root))

