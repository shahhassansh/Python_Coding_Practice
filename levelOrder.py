class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(A):
    res = []
    pre = [A]
    next_lev = []
    while pre:
        for i in range(len(pre)):
            res.append(pre[i].val)
            if pre[i].left is not None:
                next_lev.append(pre[i].left)
            if pre[i].right is not None:
                next_lev.append(pre[i].right)
        pre = next_lev
        next_lev = []

    return res

A= TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
A.left.left = TreeNode(4)
A.left.right = TreeNode(5)

print(levelOrder(A))