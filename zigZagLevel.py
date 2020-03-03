class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def zigzag(A):
    res = []
    pre = [A]
    next_lev = []
    itr = 0
    t = []
    while pre:
        for i in range(len(pre)):
            t.append(pre[i].val)
            if pre[i].left is not None:
                next_lev.append(pre[i].left)
            if pre[i].right is not None:
                next_lev.append(pre[i].right)
        if itr == 0:
            res = res + t
            itr = 1
            t = []
        elif itr == 1:
            res = res + t[::-1]
            itr = 0
            t = []
        pre = next_lev
        next_lev = []

    return res

A= TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
A.left.left = TreeNode(4)
A.left.right = TreeNode(5)

print(zigzag(A))