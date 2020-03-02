class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct(A,B):
    if not B:
        return None
    root_pos = B.index(A[0])
    new_Node = TreeNode(A[0])
    new_Node.left = construct(A[1:root_pos+1],B[:root_pos])
    new_Node.right = construct(A[root_pos+1:],B[root_pos+1:])
    return new_Node

A = [1,2,4,5,3]
B = [4,2,5,1,3]

C = construct(A,B)

print(C.val)
print(C.left.val)
print(C.right.val)
print(C.left.left.val)
print(C.left.right.val)

