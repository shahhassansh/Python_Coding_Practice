## Given a Binary Search Tree with all distinct keys, the below code implements a function 
## largestsmaller wihich returns the largest smaller number than the given number.
##
## Example:
##
## Binary Search Tree
##       20
##    9      25
##  5   12  
##     11 14
##
## Input:
##
## 17
##
## Output:
##
## 14

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_Node = Node(val)
        if self.root == None:
            self.root = new_Node
        curr = self.root
        while curr != None:
            if val < curr.key and curr.left == None:
                curr.left = new_Node
            elif val < curr.key and curr.left != None:
                curr = curr.left
            elif val > curr.key and curr.right == None:
                curr.right = new_Node
            else:
                curr = curr.right
    
    def largestSmaller(self, num):
        curr = self.root
        largestSmaller = -1
        while curr != None:
            if num < curr.key:
                curr = curr.left
            else:
                largestSmaller = curr.key
                curr = curr.right
        return largestSmaller
    
bst = BST()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11) 
bst.insert(14)

print(bst.largestSmaller(28))

