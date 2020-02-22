class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def pushAtHead(self, new_val):
        newNode = ListNode(new_val)
        temp = self.head
        newNode.next = temp
        self.head = newNode
    
    def printlList(self):
        #A = self.head
        temp = self.head
        while (temp != None):
            print(temp.val)
            temp = temp.next
        #self.head = A
    
    def lengthList(self):
        x = 0
        #A = self.head
        temp = self.head
        while (temp != None):
            x = x+1
            temp = temp.next
        return int(x)

    def intersectionOfList(self, A, B):
        diff = 0
        if A.lengthList() > B.lengthList():
            diff = A.lengthList() - B.lengthList()
            tempA = A.head
            tempB = B.head
            for i in diff:
                tempA = tempA.next
        elif A.lengthList() < B.lengthList():
            diff = B.lengthList() - A.lengthList()
            tempA= A.head
            tempB= B.head
            for i in range(diff):
                tempB = tempB.next
        else:
            tempA = A.head
            tempB = B.head
        while tempA != None:
            if tempA is tempB:
                return tempA.val
            tempA = tempA.next
            tempB = tempB.next
        return -1

if __name__ == "__main__":
    ll = LinkedList()
    ll.pushAtHead(3)
    ll.pushAtHead(5)
    ll.pushAtHead(7)
    ll.pushAtHead(1)
    ll.printlList()
    print(ll.head.val)
    print(ll.lengthList())

    ll2 = LinkedList()
    ll2.pushAtHead(15)
    ll2.pushAtHead(17)
    temp = ll2.head
    a = ll2.lengthList()-1
    print(a)
    for i in range(a):
        temp = temp.next
    temp.next = ll.head
    ll2.printlList()

    print(ll.intersectionOfList(ll,ll2))


