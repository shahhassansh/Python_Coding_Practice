# The below code adds two Numbers represented as Linked List. 
# 
# For Example
# Linked List 1:
# 7 -> 5 -> 3 -> 1
# Linked List 2:
# 7 -> 1 -> 9
# 
# Ater I run the program, The Linked List 1 becomes
# 4 -> 7 -> 2 -> 2   


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushAtHead(self, new_val):
        new_Node = ListNode(new_val)
        new_Node.next = self.head
        self.head = new_Node
    
    def printLList(self):
        temp = self.head
        while temp!=None:
            print(temp.val)
            temp=temp.next

    def addNumbers(self,A,B):
        Node1 = A
        Node2 = B
        carry = 0
        added_number = 0
        c = 0
        while (Node1.next != None and Node2.next != None):
            added_number = Node1.val + Node2.val + carry
            c = added_number%10
            carry = added_number//10
            Node1.val = c
            Node1= Node1.next
            Node2=Node2.next
        added_number = Node1.val + Node2.val+carry
        c = added_number%10
        carry = added_number//10
        Node1.val = c
        if Node1.next == None and Node2.next != None:
            Node1.next = Node2.next
            Node1 = Node1.next
            while Node1.next != None:
                added_number=Node1.val +carry
                c = added_number%10
                carry = added_number//10
                Node1.val = c
                Node1 = Node1.next
            added_number=Node1.val +carry
            c = added_number%10
            carry = added_number//10
            Node1.val = c
        elif Node1.next != None and Node2.next == None:
            Node1 = Node1.next
            while Node1.next != None:
                added_number=Node1.val +carry
                c = added_number%10
                carry = added_number//10
                Node1.val = c
                Node1 = Node1.next
            added_number=Node1.val +carry
            c = added_number%10
            carry = added_number//10
            Node1.val = c
        if carry == 1:
            added_number = carry
            c = added_number%10
            carry = added_number//10

if __name__ == "__main__":
    ll = LinkedList()
    ll.pushAtHead(1)
    ll.pushAtHead(3)
    ll.pushAtHead(5)
    ll.pushAtHead(7)

    ll2 = LinkedList()
    ll2.pushAtHead(9)
    ll2.pushAtHead(1)
    ll2.pushAtHead(7)

    ll.printLList()
    ll2.printLList()

    ll.addNumbers(ll.head,ll2.head)

    ll.printLList()



        







