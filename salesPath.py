# A node 
class Node:

  # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

def get_cheapest_cost(rootNode):
  if len(rootNode.children) == 0:
    return rootNode.cost
  else:
    minCost = float('inf')
    for i in range(0,len(rootNode.children)):
      tempCost = get_cheapest_cost(rootNode.children[i])
      minCost = min(minCost,tempCost)
  return minCost+rootNode.cost
    
root = Node(0) 
child1 = Node(5)
child2 = Node(3)
child3 = Node(6)
root.children = [child1,child2,child3]
m1 = Node(4)
m2 = Node(2)
m3 = Node(0)
m4 = Node(1)
m5 = Node(5)
m6 = Node(1)
m7 = Node(10)
m8 = Node(1)
child1.children = [m1]
child2.children = [m2, m3]
child3.children = [m4, m5]
m2.children = [m6]
m3.children = [m7]
m6.children = [m8]

print(get_cheapest_cost(root))






        