class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kthSmallest(A,B):
    curr = A
    s = []
    while curr:
        s.append(curr)
        curr=curr.left
    k = 0
    while s:
        n = s.pop()
        k = k+1

        if k == B:
            return n.val
        
        curr = n.right
        while curr:
            s.append(curr)
            curr=curr.left
    return -1

A = TreeNode(8)
A.left = TreeNode(3)
A.left.left = TreeNode(1)
A.left.right = TreeNode(6)
A.left.right.left = TreeNode(4)
A.left.right.right = TreeNode(7)
A.right = TreeNode(10)
A.right.right = TreeNode(14)
A.right.right.left = TreeNode(13)

print(kthSmallest(A,6))
