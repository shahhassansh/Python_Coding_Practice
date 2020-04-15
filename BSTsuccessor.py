## In a Binary Search Tree (BST), an Inorder Successor of a node is 
## defined as the node with the smallest key greater than the key of the input node.
## The below code returns the Inorder successor of the given node.
##
## BST:
##
##        20
##     9      25
##   5   12
##
## Input:
## 
## the node with key 5
##
## Output:
##
## 9

class Node:

  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None
    self.parent = None


def find_in_order_successor(inputNode):
    temp = inputNode
    given = inputNode.key
    if temp.right == None:

        while temp.parent !=None:

            temp = temp.parent
            if temp.key > given:
                return temp.key
        return None
    else:
        temp = temp.right
        while temp.left != None:
            print(temp.key)
            temp = temp.left
        return temp.key  

root = Node(20)
root.left = Node(9)
root.right = Node(25)
root.left.parent = root
root.right.parent = root
root.left.left = Node(5)
root.left.right = Node(12)
root.left.left.parent = root.left
root.left.right.parent = root.left

print(find_in_order_successor(root.left.left))


