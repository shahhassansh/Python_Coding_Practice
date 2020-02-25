class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushAthead(self, x):
        temp = ListNode(x)
        temp.next = self.head
        self.head = temp

    def printLList(self):
        temp = self.head
        while temp!= None:
            print(temp.val, end = "")
            print("->", end="")
            temp = temp.next
        print("None")

    def rearrangeList(self):
        temp = self.head
        odd = temp
        evenFirst = temp.next
        even = temp.next
        while temp != None and temp.next != None:
            if odd.next == None:
                odd.next = None
            else:
                odd.next = even.next
            if even.next == None:
                even.next=None
            else:
                even.next = even.next.next
            prevodd = odd
            odd = odd.next
            even = even.next
            temp = odd
        if temp == None:
            prevodd.next = evenFirst
        elif temp.next == None:
            temp.next = evenFirst
        
if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.pushAthead(6)
    ll1.pushAthead(5)
    ll1.pushAthead(4)
    ll1.pushAthead(3)
    ll1.pushAthead(2)
    ll1.pushAthead(1)

    ll1.printLList()

    ll1.rearrangeList()
    ll1.printLList()

